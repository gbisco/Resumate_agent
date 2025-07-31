from llm.openai_client import OpenAIClient

client = OpenAIClient()

response = client.chat([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Say something funny about resumes."}
])

print("Response from OpenAI:", response)
