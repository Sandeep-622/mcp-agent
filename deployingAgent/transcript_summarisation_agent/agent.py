import os
from dotenv import load_dotenv

from google.adk import Agent

load_dotenv()

root_agent = Agent(
    name="Gemini LLM FiMCP Agent",
    description="A comprehensive financial management agent that tracks user progress in achieving financial goals.",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    instruction="You are a comprehensive financial management agent that tracks user progress in achieving financial goals. You will interact with sub-agents for data analysis, predictive modeling, and financial planning.",
)