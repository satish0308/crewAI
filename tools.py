from crewai_tools import YoutubeChannelSearchTool
import os

from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACE_ACCESS_TOKEN"] =os.getenv('HF_KEY')
# llm_model = HuggingFaceEndpoint(
#     endpoint_url="meta-llama/Meta-Llama-3-8B-Instruct",
#     huggingfacehub_api_token=os.getenv('HF_KEY'),
#     task="text-generation",
#     max_new_tokens=512
# )

from langchain_huggingface.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

#yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')


# yt_tool = YoutubeChannelSearchTool(
#     config=dict(
#         llm=dict(
#             provider="huggingface", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model='meta-llama/Meta-Llama-3-8B-Instruct',
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#         embedder=dict(
#             provider="huggingface", # or openai, ollama, ...
#             config=dict(
#                 model='sentence-transformers/all-MiniLM-L6-v2',
#                 #task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )
yt_tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)