from crewai_tools import YoutubeChannelSearchTool

from langchain_community.llms import HuggingFaceEndpoint

llm_model = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token="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",
    task="text-generation",
    max_new_tokens=512
)

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')