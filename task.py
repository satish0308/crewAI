from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

## Research task
from langchain_community.llms import HuggingFaceEndpoint

llm_model = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token="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",
    task="text-generation",
    max_new_tokens=512
)

research_task=Task(
    description=(
        "Identify the video {topic}"
        "Get detiailed information about the video from the channel"
    ),
    expected_output=" A comprehensive 5 paragraph detailed explaination of the {topic} of the video"
    tools=[yt_tool],
    agents=blog_researcher,
    llm=llm_model
)

## writing task


writng_task=Task(
    description=(
        "get the info from the youtube channel topic {topic}"
    ),
    expected_output=" Summarixe the info from the youtube channel video on the topic {topic}"
    tools=[yt_tool]
    agents=blog_writer,
    async_execution=False,
    llm=llm_model,
    output_file="new_blog-post.md"
)