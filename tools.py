from crewai_tools import YoutubeChannelSearchTool

from langchain_community.llms import HuggingFaceEndpoint

llm_model = HuggingFaceEndpoint(
    endpoint_url="meta-llama/Meta-Llama-3-8B",
    huggingfacehub_api_token="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",
    task="text-generation",
    max_new_tokens=512
)

from langchain_huggingface.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

#yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')


yt_tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="huggingface", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="meta-llama/Meta-Llama-3-8B",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="huggingface", # or openai, ollama, ...
            config=dict(
                model=embeddings,
                #task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)