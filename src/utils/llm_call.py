"""
LLM utility functions for the CV screening system.
"""
import logging
from typing import Any, Dict
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

# Check required environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
model_name = os.getenv('GOOGLE_MODEL_NAME', 'gemini-2.0-flash-exp')

def get_llm() -> ChatGoogleGenerativeAI:
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.1,  # Low temperature for consistent results
        max_tokens=30000,
        timeout=60,
        convert_system_message_to_human=True,  # Gemini specific setting
        top_p=0.8,  # Controls diversity of responses
        top_k=40  # Limits vocabulary considered
    )
    return llm

def invoke_llm(prompt: str) -> str:
    """
    Invoke LLM with fallback handling for different message formats.
    
    Args:
        llm: The language model instance
        prompt: The prompt text
        
    Returns:
        Response text from the LLM
    """
    try:
        llm=get_llm()
        # Try direct invocation first (some LLMs support this)
        result = llm.invoke(prompt)
        # print("result after llm invoke:", result)
        return str(result.content)

    except Exception as e:
        print("error",e)
