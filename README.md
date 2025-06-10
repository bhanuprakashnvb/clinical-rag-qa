# Clinical RAG QA

A Retrieval-Augmented Generation (RAG) based clinical question-answering system that enables real-time, context-aware responses using LLMs. Built with LangChain, ChromaDB, Sentence Transformers, and deployed using FastAPI + Streamlit.

---

## 🚀 Features

- 🔍 **Semantic Search**: Sub-second vector-based retrieval using ChromaDB and Sentence Transformers  
- 🧠 **LLM-Powered Answers**: Contextual generation using Retrieval-Augmented Generation (RAG)  
- ⚙️ **End-to-End Pipeline**: Data ingestion, cleaning, embedding, retrieval, and response  

---

## 🧱 Tech Stack

- **LLM Integration**: LangChain, OpenAI or local models (Ollama-compatible)
- **Vector Store**: ChromaDB
- **Embeddings**: Sentence Transformers
- **Backend**: FastAPI, Streamlit
- **Utilities**: pandas, PyYAML, dotenv, tqdm

---
🧪 Getting Started
Install dependencies
pip install -r requirements.txt

Ingest and embed data
python load_data.py

Start the Streamlit UI
streamlit run app.py

Make sure you have a .env file configured with your LLM API keys (or use Ollama locally.

💡 Use Case
Ideal for clinical researchers, medical students, and professionals seeking fast, accurate, and explainable AI-powered answers to domain-specific queries.




