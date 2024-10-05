# Accessing model using langchain

from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b", temperature=0)

response = llm.invoke("What is the temperature of Mars?")
print(response)