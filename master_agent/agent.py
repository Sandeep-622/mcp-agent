"""LLM Auditor for verifying & refining LLM-generated answers using the web."""

# from google.adk.agents import SequentialAgent
from google.adk.agents import Agent

from .sub_agents.prompt import prompt_enhancer
from .sub_agents.fetchData import fetchData_agent
from .sub_agents.chartered import chartered_agent
from .sub_agents.data_analyst import data_analyst_agent
# from .sub_agents.decider import reviser_agent

master_agent = Agent(
    model='gemini-2.5-pro', # Corrected model name for example
    name='master_agent',
    instruction=(
    '''You are a master agent orchestrating a comprehensive financial data analysis workflow. Your job is to analyze the conversation history and decide on the next single action.

    **Your Logic:**
    Always follow this order, with every new prompt from the user. 
    1.  **Initial Request:** If the last message is from the user, your first step is ALWAYS to call the `prompt_enhancer`.
    2.  **After Prompt Enhancer:** If the last message is the enhanced prompt from `prompt_enhancer`, your next step is ALWAYS to call the `chartered_agent` with that enhanced prompt.
    3.  **After Chartered Agent:** If the last message is a JSON plan from `chartered_agent`, your next step is to call the `fetchData_agent`. You must pass it BOTH the enhanced prompt and the JSON data_part list from the history.
    4.  **After FetchData Agent:** If the last message is the raw data from `fetchData_agent`, your next step is to call the `data_analyst_agent` for comprehensive analysis of the fetched data.
    5.  **After Data Analyst Agent:** If the last message is the analysis from `data_analyst_agent`, your final step is to synthesize all the information, greet the user, and present the final comprehensive financial analysis in a clear, well-formatted way.
    '''
    ),
    sub_agents=[prompt_enhancer, chartered_agent, fetchData_agent, data_analyst_agent],
)

root_agent = master_agent

#  Enhance the prompt for better clarity and effectiveness, Use the prompt_enhancer sub-agent for this and return the output as it is.
#         Depending upon the prompt, you will call the chartered_agent sub-agent to get the list of tools to be used for fetching the data.