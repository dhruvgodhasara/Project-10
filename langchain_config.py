from langchain import  LLMChain, PromptTemplate
from langchain_groq import ChatGroq
from config import api_key

# Directly provide the Groq API key (Not recommended for production)
groq_api_key = api_key

# Define the prompt template
template = """You are an AI assistant helping an equity research analyst.
Given the following query, summarize the most relevant news articles.
cd
Query: {query}"""
prompt = PromptTemplate(template=template, input_variables=['query'])

# Initialize ChatGroq with the API key
llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

# Create the LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# User query (you can modify this)
user_query = "What are the latest news on Tesla?"

# Run the chain and print the response
response = llm_chain.run(user_query)
print(response)