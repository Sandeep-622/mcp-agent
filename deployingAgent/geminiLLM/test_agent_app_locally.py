import logging
import google.cloud.logging
import asyncio
import textwrap

from vertexai.preview import reasoning_engines
from agent import root_agent

# Set up both local and Google Cloud logging.
logging.basicConfig(level=logging.INFO)
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()


async def main() -> None:
    """Initializes the agent and sends a query to it."""
    agent_app = reasoning_engines.AdkApp(
        agent=root_agent,
        enable_tracing=True,
    )

    # Create a session first
    session = agent_app.create_session(user_id="u_123")

    # Use textwrap.dedent to remove leading whitespace from the multi-line string.
    prompt = textwrap.dedent("""
        My goal is to buy a house worth ₹50 lakhs in 5 years. I am 28 years old and currently earning ₹8 lakhs per year. I want to know if I am on track to achieve this goal. Please analyze my financial data and let me know my progress.
    """)

    # Use the stream_query method with session
    for event in agent_app.stream_query(
        user_id="u_123",
        session_id=session.id,
        message=prompt,
    ):
        if "content" in event and "parts" in event["content"]:
            for part in event["content"]["parts"]:
                if "text" in part:
                    logging.info(f"[local test] {part['text']}")
                    print(f"[local test] {part['text']}")
        
    cloud_logging_client.flush_handlers()


if __name__ == "__main__":
    asyncio.run(main())