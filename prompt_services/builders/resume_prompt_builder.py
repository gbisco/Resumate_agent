# prompt_services/builders/resume_prompt_builder.py

def build_resume_parser_prompt():
    with open("prompt_services/prompts/resume_parser_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()