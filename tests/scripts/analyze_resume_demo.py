import json
from resume_agent.parser import parse_resume
from resume_agent.insight_agent import analyze_resume

# Load and parse a sample resume
parsed_resume = parse_resume("assets/sample_resume.pdf")

print("Parsed Resume Preview:")
print(json.dumps(parsed_resume, indent=2))

# Optional: load job description from file
job_description = None
try:
    with open("assets/sample_job.txt", "r", encoding="utf-8") as f:
        job_description = f.read()
except FileNotFoundError:
    print("No job description provided. Continuing with resume only.\n")

# Analyze and print insights
insights = analyze_resume(parsed_resume, job_description=job_description)
print("🔍 Resume Insights:\n")
import json
print(json.dumps(insights, indent=2))
