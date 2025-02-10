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
question = "你好，请介绍一下你自己"
response = chain.invoke({"question": question})

# 打印响应内容
print(response['text'])
print(type(response['text']))
write_to_doc(response['text'])