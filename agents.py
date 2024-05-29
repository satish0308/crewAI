from crewai import Agent
from tools import yt_tool
import os

## agent 1 -> create a senior blog content researcher

from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACE_ACCESS_TOKEN"] =os.getenv('HF_KEY')
llm = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token=os.getenv('HF_KEY'),
    task="text-generation",
    max_new_tokens=512
)

blog_researcher=Agent(
    role='Blog Researcher from YouTube Videos',
    goal="Get the relevant video content for the topic from YT Channel {topic}",
    verbose=True,
    memory=True,
    backstory=(
            "Expert in  AI ML and good with recent trends in Generative ai and LLM industry "
    ),
    tools=[yt_tool],
    allow_delegation=True
)


## agent 2 -> creating a senior Blog writer agent with YT tools

blog_writer=Agent(
    role='Blog Writer',
    goal="Narrate compleeling tech stories and Get the relevant video content for the topic from YT Channel {topic}",
    verbose=True,
    memory=True,
    backstory=(
            "Expert in  AI ML and good with recent trends in Generative ai and LLM industry "
    ),
    tools=[yt_tool],
    allow_delegation=True,
)

