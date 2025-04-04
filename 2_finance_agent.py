from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools




# Load environment variables from .env file
load_dotenv()


# Create a Groq agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data"]
)


agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")
# Print the response