
import fitz  # PyMuPDF
import json
import os
from llm.llm_router import get_llm_client


DATA_DIR = "data"
PROMPT_PATH = "prompt_services/prompts/resume_parser_prompt.txt"
OUTPUT_PATH = os.path.join(DATA_DIR, "resume_data.json")
llm = get_llm_client()

def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def load_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def parse_resume(pdf_path: str):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    resume_text = extract_text_from_pdf(pdf_path)
    
    from prompt_services.builders.resume_prompt_builder import build_resume_parser_prompt
    system_prompt = build_resume_parser_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": resume_text}
    ]

    print("Sending resume to LLM...")
    response = llm.chat(messages)

    try:
        structured = json.loads(response)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(structured, f, indent=2)
        print(f"[parser.py] Resume parsed and saved to {OUTPUT_PATH}")
    except json.JSONDecodeError:
        print("[parser.py] LLM response was not valid JSON:")
        print(response)


if __name__ == "__main__":
    parse_resume("assets/sample_resume.pdf")