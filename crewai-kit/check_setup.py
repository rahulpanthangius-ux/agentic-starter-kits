"""10-second check that your key, model, and install all work.

Run:  uv run python check_setup.py
"""
import os
import sys

from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    sys.exit("GROQ_API_KEY not found. Copy .env.example to .env and paste your key.")

model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
llm = LLM(
    model=f"openai/{model}",
    base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    api_key=os.environ["GROQ_API_KEY"],
)
print(f"Model: {model}")
print("Reply:", llm.call("Reply with exactly one word: ready"))
print("CrewAI kit OK")
