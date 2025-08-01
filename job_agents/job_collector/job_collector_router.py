from typing import Literal
from job_agents.job_collector.serpapi_collector import SerpAPICollector
from job_agents.job_collector.job_collector_client import JobCollectorClient


def get_job_collector(source: Literal["serpapi"] = "serpapi") -> JobCollectorClient:
    if source == "serpapi":
        return SerpAPICollector()
    raise ValueError(f"Unsupported job source: {source}")