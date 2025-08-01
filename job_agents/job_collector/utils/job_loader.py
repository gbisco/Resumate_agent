import json
from typing import List
from job_agents.job_schema import JobPosting
from pydantic import ValidationError


def load_job_from_json(path: str) -> JobPosting:
    """
    Load a single JobPosting from a JSON file.
    Raises ValidationError if the JSON is malformed or the structure is invalid.
    """
    with open(path, "r", encoding="utf-8") as f:
        return JobPosting.model_validate_json(f.read())


def load_jobs_from_json(path: str) -> List[JobPosting]:
    """
    Load a list of JobPostings from a JSON file (array of dicts).
    Raises ValidationError if any entry is invalid.
    """
    with open(path, "r", encoding="utf-8") as f:
        job_data = json.load(f)

    return [JobPosting.model_validate(job) for job in job_data]

def load_job_from_dict(data: dict) -> JobPosting:
    """
    Load a JobPosting from a dictionary.
    Raises ValidationError if the data is invalid.
    """
    return JobPosting.model_validate(data)

def load_jobs_from_dicts(data: List[dict]) -> List[JobPosting]:
    """
    Load a list of JobPostings from a list of dictionaries.
    Skips invalid entries and prints a warning.
    """
    jobs = []
    for job in data:
        try:
            jobs.append(JobPosting.model_validate(job))
        except ValidationError as e:
            print(f"[JobLoader] Skipping invalid job entry: {e}")
    return jobs
