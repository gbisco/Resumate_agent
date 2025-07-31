import os
import json
import pytest
from resume_agent import parser

# Mock response we'll use to avoid GPT call
MOCK_LLM_RESPONSE = json.dumps({
    "name": "Gabriel Bisco",
    "email": "gabriel@example.com",
    "phone": "+1 555-123-4567",
    "skills": ["Python", "GPT", "Power BI"],
    "experience": [],
    "education": [],
    "certifications": [],
    "summary": "An AI-focused developer with resume automation expertise."
})


@pytest.fixture
def mock_llm(monkeypatch):
    class MockLLM:
        def chat(self, messages, model=None, temperature=0.3):
            return MOCK_LLM_RESPONSE

    monkeypatch.setattr(parser, "llm", MockLLM())


def test_parse_resume_creates_output_file(mock_llm, tmp_path):
    # Setup
    test_pdf = "tests/assets/sample_resume.pdf"
    os.makedirs("tests/assets", exist_ok=True)

    # Write dummy resume content into a fake PDF
    import fitz  # PyMuPDF
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 100), "Gabriel Bisco\nEmail: gabriel@example.com\nSkills: Python, GPT")
    doc.save(test_pdf)
    doc.close()

    # Redirect output path to temporary directory
    parser.DATA_DIR = tmp_path
    parser.OUTPUT_PATH = tmp_path / "resume_data.json"

    # Run
    parser.parse_resume(test_pdf)

    # Assert output file was created and matches mock
    assert os.path.exists(parser.OUTPUT_PATH)
    with open(parser.OUTPUT_PATH, "r") as f:
        result = json.load(f)
    assert result["name"] == "Gabriel Bisco"
    assert "skills" in result


def test_parse_resume_real_pdf(tmp_path):
    # Use the sample resume you just created
    test_pdf = "assets/sample_resume.pdf"
    assert os.path.exists(test_pdf), "Missing test resume PDF!"

    # Override output location for test
    parser.DATA_DIR = tmp_path
    parser.OUTPUT_PATH = tmp_path / "resume_data.json"

    # Run the parser (this uses the real LLM)
    parser.parse_resume(test_pdf)

    # Validate the result
    assert os.path.exists(parser.OUTPUT_PATH)
    with open(parser.OUTPUT_PATH, "r") as f:
        data = json.load(f)

    assert "name" in data
    assert "skills" in data
    assert isinstance(data["skills"], list)
    assert "experience" in data
    assert isinstance(data["experience"], list)
