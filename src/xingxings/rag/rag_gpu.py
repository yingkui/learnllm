from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
import torch

# 步骤 1：加载文档
loader = TextLoader("raw-data/triangle.json", encoding="utf-8")
documents = loader.load()

# 步骤 2：分段
text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# 步骤 3：生成嵌入向量
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 步骤 4：构建索引
db = FAISS.from_documents(texts, embeddings)
db.save_local("faiss_index")

# 步骤 5：加载索引
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# 加载 Hugging Face 模型
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-math-7b-instruct", torch_dtype=torch.float16)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-math-7b-instruct",
    torch_dtype=torch.float16,
    device_map="auto"
)

# 启用梯度检查点
model.gradient_checkpointing_enable()

# 创建 HuggingFacePipeline
hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=4096,  # 减少生成长度
    temperature=0.7
)

# 创建 LLM
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# 创建 RAG 链
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3})  # 仅检索前 3 个相关文档
)

# 提问
query = "新问题：在 $\triangle ABC$ 中，若 $\sin A \sin B \sin C = \dfrac{\sqrt{3}}{2}(\sin^2 A + \sin^2 B - \sin^2 C)$, 求 $C$。请写出详细的解题步骤"
result = qa.invoke(query)  # 使用 invoke 代替 run
print(result)

# 清理显存
torch.cuda.empty_cache()