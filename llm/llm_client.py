# llm/llm_client.py

from abc import ABC, abstractmethod
from typing import List, Union, Optional


class LLMClient(ABC):
    """
    Abstract base class for any LLM provider implementation.
    """

    @abstractmethod
    def chat(
        self,
        messages: List[Union[str, dict]],
        model: Optional[str] = None,
        temperature: float = 0.3
    ) -> str:
        """
        Sends a chat-style message to the LLM.

        :param messages: List of messages in OpenAI format or simplified strings.
        :param model: Optional override model name (defaults to config).
        :param temperature: Sampling temperature for creativity.
        :return: The generated response string.
        """
        pass
