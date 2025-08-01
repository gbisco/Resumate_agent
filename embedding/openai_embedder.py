from openai import OpenAI
from config.config import OPENAI_API_KEY, EMBEDDING_MODEL
from embedding.embedding_client import EmbeddingClient

class OpenAIEmbedder(EmbeddingClient):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def embed(self, texts):
        response = self.client.embeddings.create(
            input=texts,
            model=EMBEDDING_MODEL
        )
        return [d.embedding for d in response.data]