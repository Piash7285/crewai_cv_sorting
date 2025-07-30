"""
LLM utility functions for the CV screening system.
"""
import os

from crewai import LLM
from dotenv import load_dotenv
import litellm

load_dotenv()

# Check required environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
model_name = os.getenv('GOOGLE_MODEL_NAME')

def get_llm() -> LLM:
    """
    Initializes and returns an LLM instance configured with the specified model name and API key.

    Returns:
        LLM: An instance of the LLM class with the configured model, API key, temperature, and verbosity.
    """
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required")

    litellm.api_key= google_api_key
    # Use gemini/ prefix for Google AI (not google/ prefix)
    llm = LLM(
        model=f"gemini/{model_name}",
        api_key=google_api_key,
        temperature=0.3,
        # max_tokens=3000,
        verbose=True
    )

    return llm

