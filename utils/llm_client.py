# utils/llm_client.py
import os
import logging

logger = logging.getLogger("metacraft.llm_client")

class LLMClient:
    def __init__(self):
        self.provider = "openai"
        self.api_key = os.getenv("OPENAI_API_KEY")

    def set_provider(self, provider_name: str):
        self.provider = provider_name.lower()
        logger.info(f"LLM provider set to: {self.provider}")
        if self.provider == "claude":
            self.api_key = os.getenv("CLAUDE_API_KEY")
        elif self.provider == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            logger.warning(f"Unknown LLM provider '{self.provider}', defaulting to OpenAI")
            self.provider = "openai"
            self.api_key = os.getenv("OPENAI_API_KEY")

    def call(self, prompt: str):
        logger.debug(f"LLM call with prompt: {prompt}")
        example_schema = [
            {"name": "id", "type": "STRING"},
            {"name": "timestamp", "type": "STRING"},
            {"name": "source_platform", "type": "STRING"},
            {"name": "author", "type": "STRING"},
            {"name": "region", "type": "STRING"},
            {"name": "theme", "type": "STRING"},
            {"name": "intended_audience", "type": "STRING"},
        ]
        return example_schema
