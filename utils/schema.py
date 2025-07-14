# utils/schema.py
import logging

logger = logging.getLogger("metacraft.schema")

REQUIRED_FIELDS = [
    {"name": "id", "type": "STRING"},
    {"name": "timestamp", "type": "STRING"},
]

def enrich_schema_with_rules(fields, keywords, entities):
    schema = list(REQUIRED_FIELDS)

    existing = {f["name"] for f in schema}
    for field in fields:
        if field["name"] not in existing:
            schema.append(field)
            existing.add(field["name"])

    if "region" in keywords and "region" not in existing:
        schema.append({"name": "region", "type": "STRING"})
    if "audience" in keywords and "intended_audience" not in existing:
        schema.append({"name": "intended_audience", "type": "STRING"})

    entity_labels = {e["label"] for e in entities}
    if "GPE" in entity_labels and "location" not in existing:
        schema.append({"name": "location", "type": "STRING"})

    logger.debug(f"Schema after enrichment: {schema}")
    return schema
