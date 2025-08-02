# embedding/embedding_tool.py

from embedding.embedding_router import get_embedder
from resume_agents.resume_schema import Resume
from job_agents.job_schema import JobPosting

class EmbeddingTool:
    """
    EmbeddingTool wraps an embedding client (e.g. OpenAIEmbedder) to convert
    structured Resume and JobPosting objects into dense vector embeddings.
    """

    def __init__(self, embedder=None):
        """
        Initialize the embedding tool with an optional custom embedder.
        If none is provided, it uses the default configured embedder from router.
        """
        self.embedder = embedder or get_embedder()

    def embed_resume(self, resume: Resume) -> list[float]:
        """
        Converts a Resume object to an embedding vector using its __str__() format.
        :param resume: Resume object
        :return: List of floats (embedding vector)
        """
        text = str(resume)
        return self.embedder.embed([text])[0]  # [0] gets the first (and only) embedding

    def embed_job(self, job: JobPosting) -> list[float]:
        """
        Converts a JobPosting object to an embedding vector using its __str__() format.
        :param job: JobPosting object
        :return: List of floats (embedding vector)
        """
        text = str(job)
        return self.embedder.embed([text])[0]
