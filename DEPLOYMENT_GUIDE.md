# How to Deploy Your Swiggy RAG App 🚀

To show this off in an interview, you should deploy it to **Streamlit Community Cloud**. It’s free, easy, and provides a public URL anyone can access.

### 1. Upload Your Code to GitHub
1.  **Create a GitHub Repository**: Go to [github.com/new](https://github.com/new) and name it something like `swiggy-rag-app`.
2.  **Add Your Files**: Upload the following files:
    *   `app.py`
    *   `requirements.txt`
    *   `data/swiggy_report.pdf` (Wait—keep reading the note below!)
    *   `vector_store/` (Upload the entire folder)

> [!WARNING]
> **DO NOT** upload your `.env` file to GitHub. This would expose your secret API key to the public. We will handle the key safely in the deployment settings.

### 2. Deploy to Streamlit
1.  Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
2.  Click **"Create app"** and select your GitHub repository.
3.  Set the main file path to `app.py`.
4.  **Crucial Step (Secrets)**:
    *   Before clicking "Deploy", click **"Advanced settings..."**.
    *   In the **Secrets** box, paste this:
        ```toml
        GEMINI_API_KEY = "your-api-key-here"
        ```
    *   Replace `your-api-key-here` with your actual key.
5.  Click **"Deploy!"**.

### 3. Verification
*   The deployment will take 2–3 minutes to install dependencies.
*   Once finished, you’ll get a public URL (e.g., `swiggy-rag.streamlit.app`).
*   **Try it out!** Send the link to yourself or a friend to verify it works.

---

### Important Maintenance Tip
If your app crashes or can't find the `vector_store`, ensure you uploaded the *contents* of the `vector_store/` folder (the `.faiss` and `.pkl` files) exactly as they appear locally.
