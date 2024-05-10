from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI



agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
    ["C:\Development\python\koios-assistant\koios_assistant\src\data.csv", "C:\Development\python\koios-assistant\koios_assistant\src\data_two.csv"], 
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent.run("Qual a data de hoje?")