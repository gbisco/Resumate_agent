import pytest
from llm.openai_client import OpenAIClient
from types import SimpleNamespace


def test_chat_returns_string(monkeypatch):
    # Create a mock response object that mimics OpenAI's structure
    mock_response = SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(
                    content="This is a test response"
                )
            )
        ]
    )

    def mock_create(*args, **kwargs):
        return mock_response

    # Patch the OpenAI API call
    from openai import ChatCompletion
    monkeypatch.setattr(ChatCompletion, "create", mock_create)

    client = OpenAIClient()
    result = client.chat([
        {"role": "user", "content": "Hello!"}
    ])

    assert isinstance(result, str)
    assert result == "This is a test response"