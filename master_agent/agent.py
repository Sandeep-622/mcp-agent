"""LLM Auditor for verifying & refining LLM-generated answers using the web."""

# from google.adk.agents import SequentialAgent
from google.adk.agents import Agent

from .sub_agents.prompt import prompt_enhancer
from .sub_agents.fetchData import fetchData_agent
# from .sub_agents.decider import reviser_agent


master_agent = Agent(
    model='gemini-2.5-flash',
    name='master_agent',
    description=(
        '''You are a smart data fetcher. Your job is to do the following:
        1. Greet the user whenever possible. for that you don't need to call any sub-agent.
        2. Enhance the prompt for better clarity and effectiveness, Use the prompt_enhancer sub-agent for this and return the output as it is.
        3. If asked to fetch the data directly, use the fetchData_agent sub-agent.
        '''
    ),
    sub_agents=[prompt_enhancer, fetchData_agent],
)

root_agent = master_agent