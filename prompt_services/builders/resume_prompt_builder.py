import json
from jinja2 import Template

def build_resume_parser_prompt():
    with open("prompt_services/prompts/resume_parser_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def build_resume_insight_prompt(parsed_resume: dict, job_posting: dict = None) -> str:
    """
    Builds a prompt for the resume insight agent using a Jinja2 template.
    Expects structured JSON resume and (optionally) a structured job posting.
    """
    with open("prompt_services/prompts/resume_insight_prompt.txt", "r", encoding="utf-8") as f:
        template = Template(f.read())

    rendered = template.render(
        resume_json=json.dumps(parsed_resume, indent=2),
        job_json=json.dumps(job_posting, indent=2) if job_posting else None
    )
    return rendered
