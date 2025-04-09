from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat



# Load environment variables from .env file
load_dotenv()


# Create a Groq agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent1=Agent(
    model=OpenAIChat(id="gpt-4")
)    
 
agent.print_response("Write 2 sentence Love relationship between shahil and his anonymous girlfriend")
# Print the response