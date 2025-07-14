# app.py
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import logging
from agents.orchestrator import AgentOrchestrator
from exporters.bigquery_exporter import BigQueryExporter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("metacraft")

app = FastAPI(title="MetaCraft Pro API")

# Allow all origins for testing — you may restrict in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = AgentOrchestrator()
bigquery_exporter = BigQueryExporter()

# Schema for requests
class SchemaRequest(BaseModel):
    prompt: str
    llm_provider: Optional[str] = "openai"  # or "claude"
    save_name: Optional[str] = None  # name to save the schema under

class SchemaExportRequest(BaseModel):
    save_name: str
    project_id: str
    dataset_id: str
    table_id: str

# In-memory store for generated schemas (name -> schema)
SCHEMA_STORE = {}

@app.get("/")
async def root():
    return {"message": "Welcome to MetaCraft Pro API"}

@app.post("/generate-schema")
async def generate_schema(request: SchemaRequest):
    logger.info(f"Generating schema for prompt: {request.prompt}")
    try:
        schema = orchestrator.handle_request(
            prompt=request.prompt,
            llm_provider=request.llm_provider
        )
        if request.save_name:
            SCHEMA_STORE[request.save_name] = schema
            logger.info(f"Schema saved as '{request.save_name}'")
        return {"schema": schema, "saved_as": request.save_name}
    except Exception as e:
        logger.error(f"Error generating schema: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/schemas")
async def list_schemas():
    """List saved schema names."""
    return {"saved_schemas": list(SCHEMA_STORE.keys())}

@app.get("/schemas/{name}")
async def get_schema(name: str):
    schema = SCHEMA_STORE.get(name)
    if not schema:
        raise HTTPException(status_code=404, detail=f"Schema '{name}' not found")
    return {"name": name, "schema": schema}

@app.post("/export/bigquery")
async def export_bigquery(request: SchemaExportRequest):
    logger.info(f"Export request to BigQuery table: {request.project_id}.{request.dataset_id}.{request.table_id}")
    schema = SCHEMA_STORE.get(request.save_name)
    if not schema:
        raise HTTPException(status_code=404, detail=f"Schema '{request.save_name}' not found")
    try:
        job_id = bigquery_exporter.export_schema(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            table_id=request.table_id,
            schema=schema
        )
        return {"message": "Export started", "job_id": job_id}
    except Exception as e:
        logger.error(f"Error exporting to BigQuery: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
