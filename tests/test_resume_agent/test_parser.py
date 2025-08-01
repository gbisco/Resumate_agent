import os
import json
import pytest
from resume_agents import parser
from resume_agents.resume_schema import Resume

MOCK_LLM_RESPONSE = json.dumps({
    "name": "Gabriel Bisco",
    "email": "gabriel@example.com",
    "phone": "+1 555-123-4567",
    "skills": ["Python", "GPT", "Power BI"],
    "experience": [
        {
            "title": "AI Developer",
            "company": "ResumeTech Inc.",
            "dates": "Jan 2021 – Present",
            "description": "Built intelligent resume parsing and analysis tools using OpenAI APIs."
        }
    ],
    "education": [
        {
            "institution": "Georgia Tech",
            "degree": "M.S.",
            "field": "Computer Science",
            "dates": "2023 – 2025"
        }
    ],
    "certifications": [
        {
            "name": "AWS Certified Machine Learning – Specialty",
            "issuer": "Amazon Web Services",
            "date": "June 2023"
        }
    ],
    "awards": [
        {
            "title": "Dean’s List",
            "issuer": "Georgia Tech",
            "date": "Fall 2023",
            "description": "Awarded for academic excellence"
        }
    ],
    "projects": [
        {
            "name": "Resume Tailor AI",
            "description": "An AI assistant that rewrites resumes based on job descriptions.",
            "technologies": ["Python", "LangChain", "OpenAI"],
            "url": "https://github.com/gabrielbisco/resume-tailor-ai"
        }
    ],
    "summary": "An AI-focused developer with resume automation expertise."
})


@pytest.fixture
def mock_llm(monkeypatch):
    class MockLLM:
        def chat(self, messages, model=None, temperature=0.3):
            return MOCK_LLM_RESPONSE

    monkeypatch.setattr(parser, "llm", MockLLM())


def test_parse_resume_creates_output_file(mock_llm, tmp_path):
    # Create dummy PDF
    test_pdf = "tests/assets/sample_resume.pdf"
    os.makedirs("tests/assets", exist_ok=True)

    import fitz  
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 100), "Gabriel Bisco\nEmail: gabriel@example.com\nSkills: Python, GPT")
    doc.save(test_pdf)
    doc.close()

    parser.DATA_DIR = tmp_path
    parser.OUTPUT_PATH = tmp_path / "resume_data.json"

    resume = parser.parse_resume(test_pdf)

    assert isinstance(resume, Resume)
    assert resume.name == "Gabriel Bisco"
    assert "GPT" in resume.skills
    assert resume.experience[0].title == "AI Developer"
    assert resume.education[0].institution == "Georgia Tech"
    assert resume.certifications[0].name.startswith("AWS Certified")
    assert resume.projects[0].technologies == ["Python", "LangChain", "OpenAI"]

    assert os.path.exists(parser.OUTPUT_PATH)
    with open(parser.OUTPUT_PATH, "r") as f:
        result = json.load(f)
    assert result["name"] == "Gabriel Bisco"
    assert "skills" in result


def test_parse_resume_real_pdf(tmp_path):
    test_pdf = "assets/sample_resume.pdf"
    assert os.path.exists(test_pdf), "Missing test resume PDF!"

    parser.DATA_DIR = tmp_path
    parser.OUTPUT_PATH = tmp_path / "resume_data.json"

    resume = parser.parse_resume(test_pdf)

    assert isinstance(resume, Resume)
    assert resume.name
    assert isinstance(resume.skills, list)
    assert isinstance(resume.experience, list)
    assert isinstance(resume.education, list)

    assert os.path.exists(parser.OUTPUT_PATH)
    with open(parser.OUTPUT_PATH, "r") as f:
        data = json.load(f)
    assert "name" in data
    assert "skills" in data
