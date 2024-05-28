from crewai import Crew,Process
from tools import yt_tool
from agents import blog_researcher,blog_writer
from task import research_task,writng_task


from langchain_community.llms import HuggingFaceEndpoint

llm_model = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token="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",
    task="text-generation",
    max_new_tokens=512
)

crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,writng_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

##kick off the crew

result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})

print(result)