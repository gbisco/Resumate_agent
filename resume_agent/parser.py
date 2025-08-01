import fitz  # PyMuPDF
import json
import os
from llm.llm_router import get_llm_client
from resume_agent.resume_schema import Resume
from pydantic import ValidationError
from prompt_services.builders.resume_prompt_builder import build_resume_parser_prompt

# Configuration
DATA_DIR = "data"
PROMPT_PATH = "prompt_services/prompts/resume_parser_prompt.txt"
OUTPUT_PATH = os.path.join(DATA_DIR, "resume_data.json")

llm = get_llm_client()


def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])


def parse_resume(pdf_path: str) -> Resume | dict:
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    resume_text = extract_text_from_pdf(pdf_path)
    system_prompt = build_resume_parser_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": resume_text}
    ]

    print("[parser.py] Sending resume to LLM...")
    response = llm.chat(messages)

    # Try parsing JSON
    try:
        parsed_json = json.loads(response)
    except json.JSONDecodeError:
        print("[parser.py] LLM response was not valid JSON:")
        print(response)
        return {"error": "LLM returned invalid JSON", "raw_response": response}

    # Try validating the schema
    try:
        resume_obj = Resume(**parsed_json)
    except ValidationError as ve:
        print("[parser.py] Resume schema validation failed:")
        print(ve)
        return {
            "error": "Resume schema construction failed",
            "validation_errors": ve.errors(),
            "raw_data": parsed_json
        }

    # Save the clean JSON
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(resume_obj.dict(), f, indent=2)

    print(f"[parser.py] Resume parsed and saved to {OUTPUT_PATH}")
    return resume_obj


if __name__ == "__main__":
    parsed = parse_resume("assets/sample_resume.pdf")
    if isinstance(parsed, Resume):
        print(json.dumps(parsed.dict(), indent=2))
    else:
        print(parsed)
