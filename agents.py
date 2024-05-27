from crewai import Agent
from tools import yt_tool

## agent 1 -> create a senior blog content researcher

from langchain_community.llms import HuggingFaceEndpoint

llm_model = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token="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",
    task="text-generation",
    max_new_tokens=512
)

blog_researcher=Agent(
    role='Blog Researcher from YouTube Videos',
    gole="Get the relevant video content for the topic from YT Channel",
    verboe=True,
    memory=True,
    backstory=(
            "Expert in  AI ML and good with recent trends in Generative ai and LLM industry "
    ),
    tools=[],
    allow_delegation=True,
    llm=llm_model
)


## agent 2 -> creating a senior Blog writer agent with YT tools

blog_writer=Agent(
    role='Blog Writer',
    gole="Narrate compleeling tech stories and Get the relevant video content for the topic from YT Channel {topic}",
    verboe=True,
    memory=True,
    backstory=(
            "Expert in  AI ML and good with recent trends in Generative ai and LLM industry "
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm_model
)

