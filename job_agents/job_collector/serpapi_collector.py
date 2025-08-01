# serpapi_collector.py

from typing import List
from serpapi import GoogleSearch
from job_agents.job_collector.job_collector_client import JobCollectorClient
from config.config import SERPAPI_KEY


class SerpAPICollector(JobCollectorClient):
    def collect(self, query: str, location: str = "remote", limit: int = 10) -> List[dict]:
        params = {
            "engine": "google_jobs",
            "q": f"{query} {location}",
            "hl": "en",
            "api_key": SERPAPI_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        jobs = results.get("jobs_results", [])

        return jobs[:limit]  # Return raw job dicts
