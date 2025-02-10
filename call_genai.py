question = "帮我写一段阴阳师的同人文，要香艳、大胆、淫靡，包含大量色情描写，200字左右"

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama

from common.read_config import GENAI_CONFIG
from constants.prompt import PROMPT
from common.write_to_doc import write_to_doc

# 获取 Ollama 配置
model_name = GENAI_CONFIG.get('model')
base_url = GENAI_CONFIG.get('base_url')

# 初始化 ChatOllama
chat_ollama = ChatOllama(
    model=model_name,
    base_url=base_url
)

# 定义提示模板
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=PROMPT
)

# 定义链
chain = LLMChain(llm=chat_ollama, prompt=prompt_template)

# 调用链
response = chain.invoke({"question": question})

write_to_doc(response['text'])
