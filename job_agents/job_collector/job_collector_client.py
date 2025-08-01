from abc import ABC, abstractmethod
from typing import List
from job_agents.job_schema import JobPosting

class JobCollectorClient(ABC):
    @abstractmethod
    def collect(self, query: str, location: str = "remote", limit: int = 10) -> List[JobPosting]:
        pass
