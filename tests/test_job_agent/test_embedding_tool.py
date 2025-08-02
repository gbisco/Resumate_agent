import pytest
from job_agents.embedding_tool import EmbeddingTool
from resume_agents.resume_schema import Resume, ExperienceEntry
from job_agents.job_schema import JobPosting

@pytest.fixture
def tool():
    return EmbeddingTool()

def test_embed_resume_returns_vector(tool):
    resume = Resume(
        name="Alice Smith",
        email="alice@example.com",
        phone="555-1234",
        skills=["Python", "Data Science"],
        experience=[
            ExperienceEntry(
                title="Data Scientist",
                company="DataCorp",
                dates="2020–2022",
                description="Built ML pipelines."
            )
        ]
    )
    vector = tool.embed_resume(resume)
    assert isinstance(vector, list)
    assert all(isinstance(x, float) for x in vector)
    assert len(vector) > 0

def test_embed_job_returns_vector(tool):
    job = JobPosting(
        id="job001",
        title="ML Engineer",
        company_name="TechStart",
        location="Remote",
        description="Work on AI systems.",
        url="https://example.com/job001"
    )
    vector = tool.embed_job(job)
    assert isinstance(vector, list)
    assert all(isinstance(x, float) for x in vector)
    assert len(vector) > 0