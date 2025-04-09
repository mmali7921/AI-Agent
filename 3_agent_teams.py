from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo




# Load environment variables from .env file
load_dotenv()

web_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
   # show_tool_calls=True,
    markdown=True,
   # debug_mode=True,
    instructions=["Always include sources in your response"]
)

# Create a Groq agent
finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    #show_tool_calls=True,
    markdown=True,
    #debug_mode=True,
    instructions=["use tables to display data"]
)


agent_team = Agent(
    team=[web_agent, finance_agent],
    #show_tool_calls=True,
    markdown=True,
    #debug_mode=True,
    instructions=["Always include sources,use tables to display data"]
)

agent_team.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
# Print the response