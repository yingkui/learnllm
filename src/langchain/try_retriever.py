from langchain_community.embeddings import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import

# Initialize an embedding function
embedding_function = OpenAIEmbeddings()

# Load or create a vector store
documents = ["What is AI?", "Introduction to Machine Learning", "Deep Learning basics"]
db = FAISS.from_texts(documents, embedding_function)

# Use the vector store as a retriever
retriever = db.as_retriever()

# Query the retriever
query = "Tell me about artificial intelligence."
results = retriever.get_relevant_documents(query)

# Output the results
for result in results:
    print(result.page_content)
