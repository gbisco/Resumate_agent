import pytest
from llm.openai_client import OpenAIClient
from types import SimpleNamespace

def test_chat_returns_string(monkeypatch):
    # Create a mock object that replicates OpenAI's method chain
    class MockCompletions:
        def create(self, *args, **kwargs):
            return SimpleNamespace(
                choices=[SimpleNamespace(
                    message=SimpleNamespace(content="This is a test response")
                )]
            )

    class MockChat:
        completions = MockCompletions()

    class MockClient:
        chat = MockChat()

    # Instantiate normally, then patch the `.client` attribute directly
    client = OpenAIClient()
    monkeypatch.setattr(client, "client", MockClient())

    result = client.chat([{"role": "user", "content": "Hello!"}])

    assert isinstance(result, str)
    assert result == "This is a test response"