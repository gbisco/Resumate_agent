from dataclasses import dataclass, field, asdict
from typing import List, Optional


@dataclass
class Recruiter:
    name: str
    title: Optional[str] = None
    email: Optional[str] = None
    linkedin_url: Optional[str] = None

    def is_valid(self) -> bool:
        return any([self.name, self.email, self.linkedin_url])

    def to_dict(self):
        return asdict(self)


@dataclass
class JobPosting:
    id: str                      # Unique ID (can be hash, UUID, or source-specific)
    title: str                   # Job title
    company: str                 # Company name
    location: str                # e.g., "Remote", "New York, NY"
    description: str            # Full job description (used for embedding, matching)
    url: str                     # Link to apply or view posting
    source: Optional[str] = None  # "LinkedIn", "Indeed", etc.
    
    # Optional fields
    qualifications: Optional[List[str]] = field(default_factory=list)  # Parsed requirements/skills
    recruiter: Optional[Recruiter] = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "description": self.description,
            "url": self.url,
            "source": self.source,
            "qualifications": self.qualifications,
            "recruiter": self.recruiter.to_dict() if self.recruiter else None,
        }

    def short_summary(self) -> str:
        return f"{self.title} at {self.company} ({self.location})"
