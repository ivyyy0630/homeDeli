from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from common.read_config import EMBED_CONFIG
# 指定要加载的特定向量空间的路径
persist_directory = "chroma_vector_db"
collection_name = 'chengshen'

# 打印配置信息
print("EMBED_CONFIG:", EMBED_CONFIG)

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

# 进行相似性搜索
query_text = "魈和钟离"  # 查询文本

# 搜索与查询向量最相似的文档
# 参数 k 表示返回最相似的 k 个文档
results = chroma_client.similarity_search(query_text, k=10)

# 打印搜索结果
for result in results:
    print("Similar Document:", result)