import openai
from openai import OpenAI
from llm.llm_client import LLMClient
from config.config import (OPENAI_API_KEY, LLM_MODEL)

class OpenAIClient(LLMClient):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def chat(self, messages, model=LLM_MODEL, temperature=0.3):
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, str):
                formatted_messages.append({"role": "user", "content": msg})
            else:
                formatted_messages.append(msg)

        response = self.client.chat.completions.create(
            model=model,
            messages=formatted_messages,
            temperature=temperature
        )

        return response.choices[0].message.content.strip()
