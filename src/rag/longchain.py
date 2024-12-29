import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Suppress HuggingFace tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load environment variables
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize the embedding model
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Load and prepare the dataset
file_path = os.path.join(os.path.dirname(__file__), 'cat-facts.txt')
with open(file_path, 'r') as file:
    raw_text = file.read()
    print(f'Loaded text file')

# Split text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
texts = text_splitter.split_text(raw_text)
print(f'Split into {len(texts)} chunks')

# Create vector store
vectorstore = FAISS.from_texts(texts, embeddings)

# Initialize the LLM using OpenAI interface
llm = ChatOpenAI(
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com/v1",
    model_name="deepseek-chat"
)

# Create prompt template
prompt_template = """You are a helpful chatbot. Use only the following pieces of context to answer the question. Don't make up any new information:

Context: {context}

Question: {question}

Answer: """

# Create the RAG chain using RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={
        "prompt": ChatPromptTemplate.from_template(prompt_template),
    }
)

# Function to process queries
def process_query(query: str):
    try:
        response = qa_chain.invoke({"query": query})
        return response["result"]
    except Exception as e:
        return f"An error occurred: {e}"

# Interactive query loop
if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
            
        response = process_query(query)
        print("\nResponse:", response)