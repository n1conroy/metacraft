# app.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging

from agents.orchestrator import AgentOrchestrator
from exporters.bigquery_exporter import BigQueryExporter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("metacraft")

app = FastAPI(title="MetaCraft Pro API")

# CORS middleware for testing/demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = AgentOrchestrator()
bigquery_exporter = BigQueryExporter()

class SchemaRequest(BaseModel):
    prompt: str
    llm_provider: Optional[str] = "openai"
    save_name: Optional[str] = None

class SchemaExportRequest(BaseModel):
    save_name: str
    project_id: str
    dataset_id: str
    table_id: str

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
            logger.info(f"Schema
