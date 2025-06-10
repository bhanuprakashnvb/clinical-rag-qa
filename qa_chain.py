# qa_chain.py
import os
from retriever import get_chroma_collection
from cache import cache_get, cache_set
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def ask_llm(prompt):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "RAG Medical QA",
            },
            model="nousresearch/deephermes-3-mistral-24b-preview:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print("🚨 LLM API call failed:", e)
        return "Error: LLM failed to respond."

def get_answer(query):
    cached = cache_get(query)
    if cached: return cached

    retriever = get_chroma_collection()
    results = retriever.query(query_texts=[query], n_results=3)
    context = "\n".join(results['documents'][0])
    prompt = f"Answer the following medical question using the context below:\n\n{context}\n\nQuestion: {query}"

    answer = ask_llm(prompt)
    cache_set(query, answer)
    return answer