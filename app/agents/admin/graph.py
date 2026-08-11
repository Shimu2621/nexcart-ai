# LangGraph admin analytics agent — plan.txt section 6. Same shape as
# agents/customer/graph.py (langchain.agents.create_agent + the shared
# durable checkpointer from core/memory.py), but no guest path
# (admin-only, enforced by app.deps.auth.get_current_admin before this
# graph ever runs) and no rag_search tool — analytics tools only.

from langchain.agents import create_agent

import app.core.memory as memory
from app.agents.admin.prompts import SYSTEM_PROMPT
from app.agents.admin.state import AdminAgentState
from app.agents.admin.tools import build_admin_tools
from app.core.llm import get_admin_llm


def build_admin_graph():
    tools = build_admin_tools()
    llm = get_admin_llm()
    return create_agent(
        llm,
        tools=tools,
        state_schema=AdminAgentState,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory.checkpointer,
    )

# ```python
# Import LangChain's create_agent function.
# This function is used to create an AI agent that can use tools
# and interact with an LLM to answer user questions.
from langchain.agents import create_agent

# Import the shared memory module from the application's core package.
# This module contains the durable checkpointer used to save and restore
# the agent's conversation/state between requests.
import app.core.memory as memory

# Import the system prompt specifically designed for the Admin Agent.
# The system prompt tells the LLM how it should behave and what type
# of analytics questions it is responsible for answering.
from app.agents.admin.prompts import SYSTEM_PROMPT

# Import the state schema used by the Admin Analytics Agent.
# AdminAgentState defines the structure of the information/state
# maintained while the agent is running.
from app.agents.admin.state import AdminAgentState

# Import the function responsible for creating the analytics tools
# available to the Admin Agent.
# These tools may query sales, orders, products, inventory, customers, etc.
from app.agents.admin.tools import build_admin_tools

# Import the function that creates/configures the LLM used by
# the Admin Analytics Agent.
# Keeping LLM configuration in a separate module makes the code
# easier to maintain and change later.
from app.core.llm import get_admin_llm


# Define a function that builds and returns the Admin Analytics Agent.
# The function collects the LLM, tools, state schema, system prompt,
# and persistent checkpointer and combines them into one agent.
def build_admin_graph():

    # Build/load all analytics tools that the Admin Agent is allowed to use.
    # For example, these tools could provide revenue, order, product,
    # inventory, customer, and refund information.
    tools = build_admin_tools()

    # Get the LLM configured for the Admin Analytics Agent.
    # The returned LLM is responsible for reasoning about the admin's
    # question and deciding which analytics tools it needs to call.
    llm = get_admin_llm()

    # Create and return the actual Admin Analytics Agent.
    # create_agent connects the LLM with the tools, state, instructions,
    # and persistent memory configuration.
    return create_agent(

        # Pass the configured LLM to the agent.
        # The LLM handles reasoning and generates the final natural-language
        # response for the administrator.
        llm,

        # Give the agent access to the analytics tools created above.
        # The LLM can decide which tool(s) to call based on the admin's question.
        tools=tools,

        # Tell the agent which state structure/schema it should use.
        # AdminAgentState defines the data maintained during agent execution.
        state_schema=AdminAgentState,

        # Provide the system instructions for the Admin Agent.
        # These instructions control the agent's behavior, responsibilities,
        # and rules for using analytics data.
        system_prompt=SYSTEM_PROMPT,

        # Provide the shared durable checkpointer.
        # This allows the agent's state/conversation to be persisted and
        # restored when the admin sends follow-up questions.
        checkpointer=memory.checkpointer,
    )
# ```

