from google.adk.agents import Agent
from google.adk.tools import google_search
from . import prompt


chartered_agent = Agent(
    model='gemini-2.5-flash',
    name='chartered_agent',
    description="You are a specialized chartered agent. Your primary responsibility is to analyze a user's request and determine which of the following predefined tools should be invoked to fulfill the user's objective.",
    instruction=prompt.PROMPT,
    # tools=[google_search],
)

