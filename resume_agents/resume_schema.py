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

    def __str__(self) -> str:
        lines = [f"Name: {self.name}", f"Email: {self.email}", f"Phone: {self.phone}"]

        if self.summary:
            lines.append(f"\nSummary:\n{self.summary}")

        if self.skills:
            lines.append(f"\nSkills:\n- " + "\n- ".join(self.skills))

        if self.experience:
            lines.append("\nExperience:")
            for exp in self.experience:
                lines.append(f"- {exp.title} at {exp.company} ({exp.dates})\n  {exp.description}")

        if self.education:
            lines.append("\nEducation:")
            for edu in self.education:
                lines.append(f"- {edu.degree} in {edu.field} from {edu.institution} ({edu.dates})")

        if self.certifications:
            lines.append("\nCertifications:")
            for cert in self.certifications:
                line = f"- {cert.name}"
                if cert.issuer:
                    line += f", {cert.issuer}"
                if cert.date:
                    line += f" ({cert.date})"
                lines.append(line)

        if self.awards:
            lines.append("\nAwards:")
            for award in self.awards:
                line = f"- {award.title}"
                if award.issuer:
                    line += f", {award.issuer}"
                if award.date:
                    line += f" ({award.date})"
                if award.description:
                    line += f"\n  {award.description}"
                lines.append(line)

        if self.projects:
            lines.append("\nProjects:")
            for proj in self.projects:
                line = f"- {proj.name}"
                if proj.url:
                    line += f" ({proj.url})"
                if proj.technologies:
                    line += f"\n  Tech: {', '.join(proj.technologies)}"
                if proj.description:
                    line += f"\n  {proj.description}"
                lines.append(line)

        return "\n".join(lines)