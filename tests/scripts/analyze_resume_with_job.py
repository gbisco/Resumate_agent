import json
import sys
from resume_agent.parser import parse_resume
from resume_agent.insight_agent import analyze_resume

RESUME_PATH = "assets/sample_resume.pdf"
JOB_DESCRIPTION_PATH = "assets/sample_job.txt"  # You can change this to any .txt file path

def main():
    print("Parsing resume...")
    parsed = parse_resume(RESUME_PATH)

    print("Loading job description...")
    try:
        with open(JOB_DESCRIPTION_PATH, "r", encoding="utf-8") as f:
            job_description = f.read()
    except FileNotFoundError:
        print(f"Job description file not found at {JOB_DESCRIPTION_PATH}. Using None.")
        job_description = None

    print("Generating insights...")
    insights = analyze_resume(parsed, job_description)

    print("\nResume Insights:\n")
    print(json.dumps(insights, indent=2))


if __name__ == "__main__":
    main()
