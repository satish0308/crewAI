from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer
import os

## Research task
from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACE_ACCESS_TOKEN"] =os.getenv('HF_KEY')
llm = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token=os.getenv('HF_KEY'),
    task="text-generation",
    max_new_tokens=512
)

research_task=Task(
    description="Identify the video {topic} Get detiailed information about the video from the channel",
    expected_output=" A comprehensive 5 paragraph detailed explaination of the {topic} of the video",
    tools=[yt_tool],
    agent=blog_researcher
)

## writing task


writng_task=Task(
    description="get the info from the youtube channel topic {topic}",
    expected_output=" Summarixe the info from the youtube channel video on the topic {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new_blog-post.md"
)

