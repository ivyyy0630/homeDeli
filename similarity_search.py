from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from common.read_config import EMBED_CONFIG
# 指定要加载的特定向量空间的路径
persist_directory = "chroma_vector_db"


def retrieve(query_text, collection_name, k=5):

    # 配置 Embedding 和 LLM
    ollama_embeddings = OllamaEmbeddings(
        base_url=EMBED_CONFIG.get('base_url'),
        model=EMBED_CONFIG.get('model'),
    )


    # 加载特定的向量空间
    chroma_client = Chroma(
        embedding_function=ollama_embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )


    # 搜索与查询向量最相似的文档
    # 参数 k 表示返回最相似的 k 个文档
    results = chroma_client.similarity_search(query_text, k=k)

    # 打印搜索结果
    return '\n'.join([result.page_content for result in results])
