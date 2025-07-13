# schema_generator.py
# Combines LLM suggestions with rule-based and spaCy-extracted fields.

from llm_client import LLMClient
from spacy_annotator import extract_keywords
import config

class SchemaGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def generate(self, request):
        base_fields = ["id", "source", "timestamp"]
        spacy_terms = extract_keywords(request)
        llm_schema = self._llm_fields(request)

        merged = list(set(base_fields + spacy_terms + llm_schema))
        return [{"name": field, "type": "STRING"} for field in merged]

    def _llm_fields(self, request):
        prompt = (
            f"Based on the following request, suggest a metadata schema as field names only:\n\n"
            f"{request}\n\n"
            f"Respond with a list like: name, date, topic"
        )
        raw = self.llm.complete(prompt)
        return [x.strip() for x in raw.split(",") if x.strip()]
