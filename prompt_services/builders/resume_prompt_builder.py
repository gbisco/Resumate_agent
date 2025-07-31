# prompt_services/builders/resume_prompt_builder.py
import json
from jinja2 import Template
from pathlib import Path

def build_resume_parser_prompt():
    with open("prompt_services/prompts/resume_parser_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()
    
def build_resume_insight_prompt(parsed_resume: dict, job_description: str = None) -> str:
    """
    Builds a prompt for the resume insight agent using a Jinja2 template.
    """
    with open("prompt_services/prompts/resume_insight_prompt.txt", "r", encoding="utf-8") as f:
        template = Template(f.read())

    rendered = template.render(
        resume_json=json.dumps(parsed_resume, indent=2),
        job_description=job_description or "N/A"
    )
    return rendered