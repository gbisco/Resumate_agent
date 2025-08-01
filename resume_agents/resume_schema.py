# resume_agent/resume_schema.py

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional


class ExperienceEntry(BaseModel):
    title: str
    company: str
    dates: str
    description: str


class EducationEntry(BaseModel):
    institution: str
    degree: str
    field: str
    dates: str


class CertificationEntry(BaseModel):
    name: str
    issuer: Optional[str] = None
    date: Optional[str] = None


class AwardEntry(BaseModel):
    title: str
    issuer: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None


class ProjectEntry(BaseModel):
    name: str
    description: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)
    url: Optional[str] = None


class Resume(BaseModel):
    name: str
    email: EmailStr
    phone: str
    skills: List[str] = Field(default_factory=list)
    experience: List[ExperienceEntry] = Field(default_factory=list)
    education: List[EducationEntry] = Field(default_factory=list)
    certifications: List[CertificationEntry] = Field(default_factory=list)
    awards: List[AwardEntry] = Field(default_factory=list)
    projects: List[ProjectEntry] = Field(default_factory=list)
    summary: Optional[str] = None
