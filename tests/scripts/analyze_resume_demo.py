import json
from resume_agent.parser import parse_resume
from resume_agent.insight_agent import analyze_resume
from job_agent.job_schema import JobPosting

# Load and parse a sample resume
parsed_resume = parse_resume("assets/sample_resume.pdf")

print("Parsed Resume Preview:")
print(json.dumps(parsed_resume.dict(), indent=2))  # ✅ Use .dict() for serialization

# Load structured job posting from JSON
job = None
try:
    with open("assets/sample_job.txt", "r", encoding="utf-8") as f:
        job_data = json.load(f)
        job = JobPosting(**job_data)
except FileNotFoundError:
    print("No job description file found. Continuing without job context.\n")
except json.JSONDecodeError as e:
    print(f"Invalid JSON in job file: {e}")
except Exception as e:
    print(f"Failed to load job posting: {e}")

# Analyze and print insights
insights = analyze_resume(parsed_resume, job_description=job)
print("🔍 Resume Insights:\n")
print(json.dumps(insights, indent=2))
