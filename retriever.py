from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def get_chroma_collection():
    client=chromadb.Client()
    embedding_fn= SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')
    collection= client.get_or_create_collection("medquad",embedding_function=embedding_fn)
    return collection


def injest_to_chroma(df):
    collection= get_chroma_collection()
    for i, row in df.iterrows():
        collection.add(
            documents=[row["Response"]],
            metadatas=[{"Instruction": row["Instruction"]}],
            ids=[f"doc_{i}"]
        )
