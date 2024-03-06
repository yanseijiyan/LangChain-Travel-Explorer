#import libraries
import re
import os
from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.tavily_search import TavilySearchResults


# Load environment variables for secure access to API keys
load_dotenv()

# Definition of API keys for the services used
TAVILY_API = os.getenv("TAVILY_API_KEY")
OPENAI_API = os.getenv("OPENAI_API_KEY")

def setup_agent():
  # Configures the LLM agent with a specific model and temperature for text generation
  llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
  # Define the search tool with the maximum number of results
  tools = [TavilySearchResults(max_results=3)]
  # Retrieves the specific agent prompt from the LangChain hub
  prompt = hub.pull("hwchase17/openai-functions-agent") 
  # Create the agent with the OpenAI functions, the LLM model and the defined tools
  agent = create_openai_functions_agent(llm, tools, prompt)
  # Returns the agent's executor, allowing the execution of verbose actions for debugging
  return AgentExecutor(agent=agent, tools=tools, verbose=True)

def extract_cost(response):
    # Extract the cost of an answer using a regular expression
    cost_str = re.search(r"\$\d+", response)
    if cost_str:
        return float(cost_str.group(0)[1:])
    return 0


def get_travel_suggestions(origin, destination, budget, interests):
    # Configure the agent for use
    agent_executor = setup_agent()
    # Query for the estimated travel cost
    travel_cost_query = f"Estimate travel cost from {origin} to {destination}."   
    travel_cost_response = agent_executor.invoke({"input": travel_cost_query})
    # Extract the cost from the response
    travel_cost = extract_cost(travel_cost_response["output"])
    # Adjust the budget based on the travel cost
    adjusted_budget = budget - travel_cost
    if adjusted_budget <= 0:
        return "The cost of travel exceeds your budget."
    # Logic to obtain destination suggestions based on the adjusted budget and interests
    trip_plan_query = f"Plan a trip to {destination} from {origin} with a budget of {adjusted_budget} and interests in {' '.join(interests)}."
    response = agent_executor.invoke({"input": trip_plan_query})
    return response["output"]