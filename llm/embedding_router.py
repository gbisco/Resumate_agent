from config.config import EMBEDDING_PROVIDER
from llm.openai_embedder import OpenAIEmbedder

def get_embedder():
    if EMBEDDING_PROVIDER == "openai":
        return OpenAIEmbedder()
    raise ValueError(f"Unsupported EMBEDDING_PROVIDER: {EMBEDDING_PROVIDER}")