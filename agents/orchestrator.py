
# agents/orchestrator.py
import logging
from llm_client import LLMClient
from nlp_utils import extract_keywords_and_entities
from schema_utils import enrich_schema_with_rules

logger = logging.getLogger("metacraft.orchestrator")

class AgentOrchestrator:
    def __init__(self):
        # Initialize LLM client, default OpenAI
        self.llm_client = LLMClient()

    def handle_request(self, prompt: str, llm_provider: str = "openai"):
        logger.info(f"Handling request with LLM provider: {llm_provider}")
        # Select LLM provider
        self.llm_client.set_provider(llm_provider)

        # Step 1: Call LLM to generate candidate fields (simulate or real)
        candidate_fields = self.llm_client.call(prompt)

        # Step 2: Use NLP to validate and extract keywords/entities
        keywords, entities = extract_keywords_and_entities(prompt)

        # Step 3: Postprocess: enrich with fixed fields & rules
        schema = enrich_schema_with_rules(candidate_fields, keywords, entities)

        logger.info(f"Generated schema with {len(schema)} fields")
        return schema
