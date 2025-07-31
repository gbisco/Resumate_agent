# llm/llm_router.py

from config.config import LLM_PROVIDER

# Import all known implementations
from llm.openai_client import OpenAIClient
# from llm.azure_client import AzureOpenAIClient  # (future)
# from llm.local_client import LocalLLMClient     # (future)

def get_llm_client():
    """
    Factory function to return the appropriate LLM client based on config.
    """
    if LLM_PROVIDER == "openai":
        return OpenAIClient()
    
    # Future extensions:
    # elif LLM_PROVIDER == "azure":
    #     return AzureOpenAIClient()
    # elif LLM_PROVIDER == "local":
    #     return LocalLLMClient()
    
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
