"""LLM Auditor for verifying & refining LLM-generated answers using the web."""

from google.adk.agents import SequentialAgent

from .sub_agents.prompt import prompt_enhancer
# from .sub_agents.decider import reviser_agent


master_agent = SequentialAgent(
    name='llm_auditor',
    description=(
        'Evaluates LLM-generated answers, verifies actual accuracy using the'
        ' web, and refines the response to ensure alignment with real-world'
        ' knowledge.'
    ),
    sub_agents=[prompt_enhancer],
)

root_agent = master_agent