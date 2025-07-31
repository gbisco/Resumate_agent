import pytest
import json
from resume_agent.insight_agent import analyze_resume


@pytest.fixture
def sample_parsed_resume():
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "skills": ["Python", "Machine Learning", "Data Analysis"],
        "experience": [
            {
                "company": "Acme Inc.",
                "title": "Data Scientist",
                "duration": "2 years",
                "description": "Built ML models for business forecasting"
            }
        ],
        "education": [
            {
                "school": "MIT",
                "degree": "MSc Computer Science"
            }
        ]
    }


def test_analyze_resume_returns_valid_json(monkeypatch, sample_parsed_resume):
    mock_response = json.dumps({
        "summary": "Strong Python and ML background",
        "suggestions": ["Add more cloud experience", "Quantify project impact"]
    })

    class MockClient:
        def chat(self, messages):
            return mock_response  # directly return the fake JSON string

    from resume_agent import insight_agent
    monkeypatch.setattr(insight_agent, "OpenAIClient", lambda: MockClient())

    result = analyze_resume(sample_parsed_resume)

    assert isinstance(result, dict)
    assert "summary" in result
    assert "suggestions" in result
