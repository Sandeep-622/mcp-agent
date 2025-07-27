import os
from dotenv import load_dotenv
import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

import vertexai
from vertexai import agent_engines

# Load environment variables and initialize Vertex AI
load_dotenv()
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
location = os.environ["GOOGLE_CLOUD_LOCATION"]
app_name = os.environ.get("APP_NAME", "Gemini LLM FiMCP")
bucket_name = f"gs://{project_id}-bucket"

# Initialize Google Cloud Logging with the correct project ID
cloud_logging_client = google.cloud.logging.Client(project=project_id)
handler = CloudLoggingHandler(cloud_logging_client, name="fimcp-agent")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)

# Initialize Vertex AI with the correct project and location
vertexai.init(
    project=project_id,
    location=location,
    staging_bucket=bucket_name,
)

# Filter agent engines by the app name in .env
ae_apps = agent_engines.list(filter=f'display_name="{app_name}"')
remote_app = next(ae_apps)

logging.info(f"Using remote app: {remote_app.display_name}")

# Get a session for the remote app
remote_session = remote_app.create_session(user_id="u_456")

# Test query with financial goal
financial_goal_query = """
My goal is to buy a house worth ₹50 lakhs in 5 years. I am 28 years old and currently earning ₹8 lakhs per year. I want to know if I am on track to achieve this goal. Please analyze my financial data and let me know my progress.
"""

# Run the agent with the financial goal query
events = remote_app.stream_query(
    user_id="u_456",
    session_id=remote_session["id"],
    message=financial_goal_query,
)

# Print responses
for event in events:
    for part in event["content"]["parts"]:
        if "text" in part:
            response_text = part["text"]
            print("[remote response]", response_text)
            logging.info("[remote response] " + response_text)

cloud_logging_client.flush_handlers()