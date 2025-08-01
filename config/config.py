import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")

EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
JOB_COLLECTOR_PROVIDER = os.getenv("JOB_COLLECTOR_PROVIDER", "serpapi")