from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Note: Adjusted the path to point to data/swiggy_report.pdf based on your directory structure
loader = PyPDFLoader("data/swiggy_report.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.from_documents(chunks, embedding_model)

vector_db.save_local("vector_store")

print("Vector database created successfully")
