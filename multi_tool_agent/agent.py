"""
Script to use ADK for creating agents
"""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from google.adk.runners import Runner
from google.adk.sessions import Session
from google.adk.memory import InMemoryMemoryService

# Set the agent model
# GEMMA_MODEL_NAME = "ollama/llama3.2:latest"
GEMMA_MODEL_NAME = "ollama/gemma3:latest"

session_service = InMemoryMemoryService()
APP_NAME = "Multi Tool Agent"
USER_ID = "Agent_One"
SESSION_ID = "Session_One"

session = Session(
    app_name=APP_NAME,
    user_id=USER_ID,
    id=SESSION_ID,
)
session_service.add_session_to_memory(session)


# Required for ADK
root_agent = Agent(
    name="Root_Agent",
    model=LiteLlm(model=GEMMA_MODEL_NAME),
    description="The main agent providing responses in German, greetings and farewells.",
    instruction="""
        You are an agent with the primary responsibility to respond to queries from the user in German.
        You simply respond the same sentence that the user provides in German.
        """,
)

runner_root = Runner(
    app_name=APP_NAME,
    session_service=session,
    agent=root_agent,
)

# from google.adk.agents import Agent
# from google.adk.tools import google_search

# root_agent = Agent(
#     # A unique name for the agent.
#     name="basic_search_agent",
#     # The Large Language Model (LLM) that agent will use.
#     model="gemini-2.0-flash-exp",
#     # A short description of the agent's purpose.
#     description="Agent to answer questions using Google Search.",
#     # Instructions to set the agent's behavior.
#     instruction="You are an expert researcher. You always stick to the facts.",
#     # Add google_search tool to perform grounding with Google search.
#     tools=[google_search],
# )
