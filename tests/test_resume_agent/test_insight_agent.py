import pytest
import json
from resume_agents.insight_agent import analyze_resume
from resume_agents.resume_schema import Resume


@pytest.fixture
def sample_parsed_resume():
    return Resume(
        name="John Doe",
        email="john@example.com",
        phone="+1 555-111-2222",
        skills=["Python", "Machine Learning", "Data Analysis"],
        experience=[
            {
                "title": "Data Scientist",
                "company": "Acme Inc.",
                "dates": "Jan 2021 – Dec 2022",
                "description": "Built ML models for business forecasting"
            }
        ],
        education=[
            {
                "institution": "MIT",
                "degree": "MSc",
                "field": "Computer Science",
                "dates": "2018 – 2020"
            }
        ],
        certifications=[],
        awards=[],
        projects=[],
        summary="Experienced data scientist with a focus on business impact."
    )


def test_analyze_resume_returns_valid_json(monkeypatch, sample_parsed_resume):
    mock_response = json.dumps({
        "candidate_summary": "Experienced data scientist with a background in machine learning and Python.",
        "top_strengths": [
            "Strong Python skills",
            "Experience building ML models"
        ],
        "weaknesses_or_gaps": [
            "Limited experience with cloud platforms"
        ],
        "improvement_suggestions": [
            "Add cloud computing certifications"
        ],
        "notable_projects": [],
        "job_match_analysis": {
            "match_rating": "Medium",
            "alignment_notes": "Relevant experience in ML, but lacks cloud exposure."
        }
    })

    class MockClient:
        def chat(self, messages):
            return mock_response  # Simulate the LLM returning valid JSON

    from resume_agents import insight_agent
    monkeypatch.setattr(insight_agent, "OpenAIClient", lambda: MockClient())

    result = analyze_resume(sample_parsed_resume)

    assert isinstance(result, dict)
    assert "candidate_summary" in result
    assert "top_strengths" in result
    assert "weaknesses_or_gaps" in result
    assert "job_match_analysis" in result
    assert result["job_match_analysis"]["match_rating"] in ["High", "Medium", "Low", None]
