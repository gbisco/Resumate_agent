import json
import re
from llm.openai_client import OpenAIClient
from resume_agent.resume_schema import Resume
from prompt_services.builders.resume_prompt_builder import build_resume_insight_prompt
from job_agent.job_schema import JobPosting



def analyze_resume(parsed_resume: Resume, job_description: JobPosting = None) -> dict:
    """
    Generate insights from a parsed resume (and optionally a job description).

    Args:
        parsed_resume (Resume): A validated Resume object.
        job_description (str, optional): Raw job description string for alignment.

    Returns:
        dict: Structured insights from the LLM.
    """
    prompt = build_resume_insight_prompt(parsed_resume.dict(), job_description.description if job_description else None)
    client = OpenAIClient()
    result = client.chat([{"role": "user", "content": prompt}])

    # Strip markdown-style JSON fences if present
    cleaned = re.sub(r"```(?:json)?\n([\s\S]*?)\n```", r"\1", result.strip())

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "error": "Could not parse LLM response",
            "raw_response": result
        }


if __name__ == "__main__":
    from resume_agent.parser import parse_resume
    parsed = parse_resume("assets/sample_resume.pdf")
    if isinstance(parsed, Resume):
        insights = analyze_resume(parsed)
        print(json.dumps(insights, indent=2))
    else:
        print("Parsing failed:", parsed)
