import json
from resume_agent.parser import parse_resume
from resume_agent.insight_agent import analyze_resume
from job_agent.job_schema import JobPosting

RESUME_PATH = "assets/sample_resume.pdf"
JOB_DESCRIPTION_PATH = "assets/sample_job.txt"  # JSON format expected

def main():
    print("Parsing resume...")
    parsed_resume = parse_resume(RESUME_PATH)

    print("Parsed Resume:")
    print(json.dumps(parsed_resume.dict(), indent=2))

    print("Loading job description...")
    job = None
    try:
        with open(JOB_DESCRIPTION_PATH, "r", encoding="utf-8") as f:
            job_data = json.load(f)
            job = JobPosting(**job_data)
    except FileNotFoundError:
        print(f"Job description file not found at {JOB_DESCRIPTION_PATH}. Continuing without it.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in job file: {e}")
    except Exception as e:
        print(f"Error loading job: {e}")

    print("Generating insights...")
    insights = analyze_resume(parsed_resume, job)

    print("\nResume Insights:\n")
    print(json.dumps(insights, indent=2))

if __name__ == "__main__":
    main()
