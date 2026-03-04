import streamlit as st
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Gemini API key not set. Please set it in the .env file.")
    st.stop()
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-flash")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load saved vector database
vector_db = FAISS.load_local(
    "vector_store",
    embedding_model,
    allow_dangerous_deserialization=True
)

st.title("📄 Swiggy Annual Report Assistant")
st.write("Ask a question about the Swiggy Annual Report.")

query = st.text_input("Enter your question")

if query:
    results = vector_db.similarity_search(query, k=7)

    context = "\n\n".join([doc.page_content for doc in results])

    prompt = f"""
    Answer the question using only the context below.

    Context:
    {context}

    Question:
    {query}
    
    Answer clearly:
    """

    response = model.generate_content(prompt)

    st.subheader("Answer")
    st.write(response.text)
