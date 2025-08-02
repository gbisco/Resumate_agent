from pydantic import BaseModel, HttpUrl, EmailStr, Field
from typing import Optional, List
import json
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

    def __str__(self) -> str:
        base_fields = self.model_dump()
        extra_fields = getattr(self, "__pydantic_extra__", {}) or {}

        all_fields = {**base_fields, **extra_fields}

        lines = []
        for key, value in all_fields.items():
            # Handle lists, dicts, and None cleanly
            if isinstance(value, list):
                value_str = ", ".join(str(v) for v in value)
            elif isinstance(value, dict):
                value_str = json.dumps(value, indent=2)
            else:
                value_str = str(value) if value is not None else "N/A"
            lines.append(f"{key}: {value_str}")

        return "\n".join(lines)

    def short_summary(self) -> str:
        return f"{self.title} at {self.company_name} ({self.location})"
