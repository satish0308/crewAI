from crewai import Crew,Process
from tools import yt_tool
from agents import blog_researcher,blog_writer
from task import research_task,writng_task
import os
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
os.environ["HUGGINGFACE_ACCESS_TOKEN"] =os.getenv('HF_KEY')
# os.environ["OPENAI_API_KEY"]=""
# # os.environ["OPENAI_MODEL_NAME"]='llama3-8b-8192'
# # os.environ["OPENAI_API_BASE"]="https://api.groq.com/openai/v1"
# from langchain_community.llms import HuggingFaceEndpoint

# llm = HuggingFaceEndpoint(
#     endpoint_url="meta-llama/Meta-Llama-3-8B-Instruct",
#     huggingfacehub_api_token=os.getenv('HF_KEY'),
#     task="text-generation",
#     max_new_tokens=512
# )
os.environ['OPENAI_API_BASE']='http://localhost:11434'
os.environ['OPENAI_MODEL_NAME']='llama3.1'  # Adjust based on available model
os.environ['OPENAI_API_KEY']='' # No API Key required for Ollama


llm = ChatOpenAI(
    model = "llama2",
    base_url = "http://localhost:11434",
    api_key="NA")

crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,writng_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    full_output=True,
    memory=True,
    cache=True,
    max_rpm =100,
    share_crew=True,
    verbose=True,
    manager_llm=llm,
    planning_llm=llm,
    )



##kick off the crew

result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})

print(result)