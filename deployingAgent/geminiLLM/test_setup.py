"""
Test script to verify the geminiLLM agent setup for goal tracking
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to the Python path
sys.path.append(os.path.dirname(__file__))

# Load environment variables
load_dotenv()

try:
    from agent import root_agent
    print("✅ Agent imported successfully!")
    print(f"Agent name: {root_agent.name}")
    print(f"Agent description: {root_agent.description}")
    print(f"Sub-agents: {len(root_agent.sub_agents) if hasattr(root_agent, 'sub_agents') and root_agent.sub_agents else 0}")
    
    # Test the basic structure
    if hasattr(root_agent, 'sub_agents') and root_agent.sub_agents:
        print(f"Sub-agent: {root_agent.sub_agents[0].name}")
        print("✅ Setup looks correct!")
    else:
        print("⚠️  No sub-agents found")
        
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
