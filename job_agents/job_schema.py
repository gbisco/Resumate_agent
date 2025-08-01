from pydantic import BaseModel, HttpUrl, EmailStr, Field
from typing import Optional, List
import uuid


class Recruiter(BaseModel):
    name: str
    title: Optional[str] = None
    email: Optional[EmailStr] = None
    linkedin_url: Optional[HttpUrl] = None

    def is_valid(self) -> bool:
        return bool(self.name or self.email or self.linkedin_url)


class JobPosting(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    company_name: str
    location: str
    description: Optional [str] = None
    url: Optional[HttpUrl] = None
    source: Optional[str] = None
    qualifications: List[str] = []
    recruiter: Optional[Recruiter] = None
    raw_google_data: Optional[dict] = None


    model_config = {
        "extra": "allow"  # allow unknown fields in dict input
    }

    def short_summary(self) -> str:
        return f"{self.title} at {self.company} ({self.location})"
