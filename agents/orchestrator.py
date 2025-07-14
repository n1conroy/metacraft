# agents/orchestrator.py
import logging
from utils.llm_client import LLMClient
from utils.nlp import extract_keywords_and_entities
from utils.schema import enrich_schema_with_rules

logger = logging.getLogger("metacraft.orchestrator")

class AgentOrchestrator:
    def __init__(self):
        self.llm_client = LLMClient()

    def handle_request(self, prompt: str, llm_provider: str = "openai"):
        logger.info(f"Handling request with LLM provider: {llm_provider}")
        self.llm_client.set_provider(llm_provider)

        candidate_fields = self.llm_client.call(prompt)
        keywords, entities = extract_keywords_and_entities(prompt)
        schema = enrich_schema_with_rules(candidate_fields, keywords, entities)

        logger.info(f"Generated schema with {len(schema)} fields")
        return schema
