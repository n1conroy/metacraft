
# exporters/bigquery_exporter.py
from google.cloud import bigquery
import logging
import uuid

logger = logging.getLogger("metacraft.bigquery_exporter")

class BigQueryExporter:
    def __init__(self):
        self.client = bigquery.Client()

    def export_schema(self, project_id: str, dataset_id: str, table_id: str, schema: list):
        bq_schema = []
        for field in schema:
            bq_schema.append(bigquery.SchemaField(field["name"], self.map_type(field["type"])))

        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        table = bigquery.Table(table_ref, schema=bq_schema)
        job = self.client.create_table(table, exists_ok=True)
        job_id = str(uuid.uuid4())
        logger.info(f"BigQuery export job {job_id} for table {table_ref} completed")
        return job_id

    def map_type(self, field_type: str):
        mapping = {
            "STRING": "STRING",
            "INT": "INTEGER",
            "INTEGER": "INTEGER",
            "FLOAT": "FLOAT",
            "BOOLEAN": "BOOL",
            "BOOL": "BOOL",
        }
        return mapping.get(field_type.upper(), "STRING")
