import os
source_folder = "results"
from langchain.document_loaders import Docx2txtLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain_experimental.text_splitter import SemanticChunker

from common.read_config import EMBED_CONFIG

# 配置 Embedding 和 LLM
ollama_embeddings = OllamaEmbeddings(
    base_url=EMBED_CONFIG.get('base_url'),
    model=EMBED_CONFIG.get('model')
)

documents = []
for filename in os.listdir(source_folder):
    if filename.endswith(".docx"):
        file_path = os.path.join(source_folder, filename)
        loader = Docx2txtLoader(file_path)
        doc = loader.load()
        documents.extend(doc)

text_splitter = SemanticChunker(
    embeddings=ollama_embeddings,
    breakpoint_threshold_type="percentile",  # 可选：percentile, standard_deviation, interquartile
    breakpoint_threshold_amount=95.0,  # 可根据需要调整
    number_of_chunks=None,  # 可选：指定分块数量
    sentence_split_regex=r"(?<=[。！？])\s*"  # 可根据需要调整句子分隔符
)
chunked_documents = text_splitter.split_documents(documents)

# 使用 Chroma 的持久化客户端保存嵌入结果
persist_directory = "chroma_vector_db"  # 指定保存路径
chroma_client = Chroma.from_documents(
    documents=chunked_documents,
    embedding=ollama_embeddings,
    persist_directory=persist_directory  # 指定持久化路径
)

# 保存嵌入结果到本地
chroma_client.persist()  # 持久化数据到指定路径

print(f"嵌入结果已保存到本地目录：{persist_directory}")