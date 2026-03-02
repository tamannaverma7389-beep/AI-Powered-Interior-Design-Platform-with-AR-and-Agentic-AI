from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

def book_furniture_tool(item):
    return f"{item} booked successfully!"

tools = [
    Tool(
        name="FurnitureBooking",
        func=book_furniture_tool,
        description="Books selected furniture item"
    )
]

llm = OpenAI(temperature=0.7)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    memory=memory,
    verbose=True
)

def run_buddy_agent(user_input):
    return agent.run(user_input)