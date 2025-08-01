import json
from job_agents.job_collector.serpapi_collector import SerpAPICollector

def test_serpapi_collector_preview():
    collector = SerpAPICollector()
    query = "machine learning engineer"
    location = "remote"

    print(f"🔍 Querying SerpAPI for: '{query}' in '{location}'...")
    jobs = collector.collect(query=query, location=location, limit=1)

    print(f"\n✅ Retrieved {len(jobs)} job(s):\n")

    for idx, job in enumerate(jobs, start=1):
        print(f"--- Job #{idx} ---")
        print("🧠 Title:", job.get("title"))
        print("🏢 Company:", job.get("company_name"))
        print("📍 Location:", job.get("location"))
        print("🔗 URL:", job.get("job_google_link", "N/A"))
        print("📝 Snippet:\n", job.get("description", "")[:250], "...\n")
        print("🧾 Full JSON:\n", json.dumps(job, indent=2)[:500], "...\n")

    # print keys and values for one job
    if jobs:
        for job in jobs:
            print("\n🔑 Job Keys and Values:")
            for key, value in job.items():
                print(f"{key}: {value if isinstance(value, str) else json.dumps(value, indent=2)}")
if __name__ == "__main__":
    test_serpapi_collector_preview()