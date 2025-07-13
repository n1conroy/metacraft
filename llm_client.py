# llm_client.py
# Provides abstraction for OpenAI or Claude completions.

import requests
import config
import openai

class LLMClient:
    def __init__(self):
        self.provider = config.LLM_PROVIDER
        self.api_key = config.API_KEY

    def complete(self, prompt):
        if self.provider == "openai":
            return self._openai(prompt)
        elif self.provider == "claude":
            return self._claude(prompt)
        return self._mock(prompt)

    def _openai(self, prompt):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=600
        )
        return response["choices"][0]["message"]["content"]

    def _claude(self, prompt):
        headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json"
        }
        data = {
            "model": "claude-2.1",
            "prompt": f"Human: {prompt}\nAssistant:",
            "max_tokens_to_sample": 600
        }
        response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=data)
        return response.json().get("completion", "")

    def _mock(self, prompt):
        return f"Mock response for prompt: {prompt}"
