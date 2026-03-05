# 📄 Swiggy Annual Report Assistant (RAG)

A production-style Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the Swiggy Annual Report and get accurate, context-aware answers using Google's Gemini LLM.

## 🚀 Live Demo
[Insert your Streamlit Cloud URL here once deployed!]

## 🛠️ Features
- **Retrieval-Augmented Generation (RAG):** Uses a vector database to retrieve relevant context before generating answers, minimizing hallucinations.
- **Efficient Document Processing:** Loads and chunks the Swiggy Annual Report PDF for optimized retrieval.
- **High-Performance Embeddings:** Uses `sentence-transformers/all-MiniLM-L6-v2` for fast and accurate semantic search.
- **Modern Web Interface:** Built with Streamlit for a clean and interactive user experience.
- **Advanced LLM:** Powered by Google's `gemini-1.5-flash` model.

## 🏗️ Architecture
1.  **Ingestion:** PDF is loaded and split into semantic chunks.
2.  **Indexing:** Chunks are converted into embeddings and stored in a **FAISS** vector store.
3.  **Retrieval:** User queries are matched against the vector store to find the most relevant chunks.
4.  **Generation:** The query + retrieved context is sent to **Gemini API** to produce a factual response.

## 💻 Tech Stack
- **Framework:** [LangChain](https://www.langchain.com/)
- **LLM:** [Google Gemini API](https://aistudio.google.com/)
- **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss)
- **Embeddings:** HuggingFace (`sentence-transformers`)
- **UI:** [Streamlit](https://streamlit.io/)

## ⚙️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nemo-0904/RAG_BASED_AI_APPLICATION.git
    cd RAG_BASED_AI_APPLICATION
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your Gemini API Key:
    ```bash
    GEMINI_API_KEY=your_api_key_here
    ```

4.  **Process the PDF (if needed):**
    If the `vector_store` is not present, run the ingestion script:
    ```bash
    python ingest.py
    ```

5.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Created for internship and portfolio purposes.*
