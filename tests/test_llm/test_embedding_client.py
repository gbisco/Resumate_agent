import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_embedder():
    mock = MagicMock()
    mock.embed.return_value = [[1.0, 2.0, 3.0]]
    return mock


def test_embedding_client_uses_default_router(monkeypatch, mock_embedder):
    monkeypatch.setattr("llm.embedding_router.get_embedder", lambda: mock_embedder)

    # Import AFTER monkeypatching
    from llm.embedding_router import get_embedder

    client = get_embedder()
    result = client.embed(["hello world"])

    assert isinstance(result, list)
    assert isinstance(result[0], list)
    assert result == [[1.0, 2.0, 3.0]]


def test_embedding_client_embed_called_correctly(monkeypatch, mock_embedder):
    monkeypatch.setattr("llm.embedding_router.get_embedder", lambda: mock_embedder)

    # Import AFTER monkeypatching
    from llm.embedding_router import get_embedder

    client = get_embedder()
    client.embed(["This is a test."])

    mock_embedder.embed.assert_called_once_with(["This is a test."])
