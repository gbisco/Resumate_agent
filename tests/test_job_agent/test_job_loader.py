import pytest
import json
from job_agents.job_collector.utils.job_loader import load_job_from_json, load_jobs_from_json, load_job_from_dict, load_jobs_from_dicts
from job_agents.job_schema import JobPosting
from pydantic import ValidationError
from pathlib import Path


def test_load_single_valid_job(tmp_path):
    job_dict = {
        "id": "job001",
        "title": "AI Engineer",
        "company_name": "OpenAI",
        "location": "Remote",
        "description": "Work with LLMs",
        "url": "https://example.com/job001"
    }
    file_path = tmp_path / "job.json"
    file_path.write_text(json.dumps(job_dict), encoding="utf-8")

    job = load_job_from_json(str(file_path))
    assert isinstance(job, JobPosting)
    assert job.title == "AI Engineer"


def test_load_multiple_jobs(tmp_path):
    job_list = [
        {
            "id": "job001",
            "title": "AI Engineer",
            "company_name": "OpenAI",
            "location": "Remote",
            "description": "Work with LLMs",
            "url": "https://example.com/job001"
        },
        {
            "id": "job002",
            "title": "ML Researcher",
            "company_name": "DeepMind",
            "location": "London",
            "description": "Research AI alignment",
            "url": "https://example.com/job002"
        }
    ]
    file_path = tmp_path / "jobs.json"
    file_path.write_text(json.dumps(job_list), encoding="utf-8")

    jobs = load_jobs_from_json(str(file_path))
    assert len(jobs) == 2
    assert all(isinstance(j, JobPosting) for j in jobs)

def test_load_single_valid_job(tmp_path):
    job_dict = {
        "id": "job001",
        "title": "AI Engineer",
        "company_name": "OpenAI",
        "location": "Remote",
        "description": "Work with LLMs",
        "url": "https://example.com/job001"
    }
    file_path = tmp_path / "job.json"
    file_path.write_text(json.dumps(job_dict), encoding="utf-8")

    job = load_job_from_json(str(file_path))
    assert isinstance(job, JobPosting)
    assert job.title == "AI Engineer"


def test_load_multiple_jobs(tmp_path):
    job_list = [
        {
            "id": "job001",
            "title": "AI Engineer",
            "company_name": "OpenAI",
            "location": "Remote",
            "description": "Work with LLMs",
            "url": "https://example.com/job001"
        },
        {
            "id": "job002",
            "title": "ML Researcher",
            "company_name": "DeepMind",
            "location": "London",
            "description": "Research AI alignment",
            "url": "https://example.com/job002"
        }
    ]
    file_path = tmp_path / "jobs.json"
    file_path.write_text(json.dumps(job_list), encoding="utf-8")

    jobs = load_jobs_from_json(str(file_path))
    assert len(jobs) == 2
    assert all(isinstance(j, JobPosting) for j in jobs)


def test_invalid_job_raises_error(tmp_path):
    bad_job = {
        "id": "bad001",
        "company_name": "Missing title and description"
    }
    file_path = tmp_path / "bad_job.json"
    file_path.write_text(json.dumps(bad_job), encoding="utf-8")

    with pytest.raises(ValidationError):
        load_job_from_json(str(file_path))

def test_load_job_from_dict_valid():
    job_dict = {
        "title": "Data Scientist",
        "company_name": "Anthropic",
        "location": "San Francisco",
        "description": "Research safety in AI",
        "url": "https://example.com/job003"
    }
    job = load_job_from_dict(job_dict)
    assert isinstance(job, JobPosting)
    assert job.company_name == "Anthropic"


def test_load_jobs_from_dicts_skips_invalid():
    jobs = [
        {
            "title": "NLP Engineer",
            "company_name": "HuggingFace",
            "location": "Remote",
            "description": "Build Transformers",
            "url": "https://example.com/job004"
        },
        {
            "id": "bad002",
            "location": "Unknown"
        }
    ]
    results = load_jobs_from_dicts(jobs)
    assert len(results) == 1
    assert results[0].title == "NLP Engineer"