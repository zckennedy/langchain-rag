import uuid
from langchain_ollama import OllamaEmbeddings
from langchain_milvus import Milvus
import pdf_loader
import splitter

URI = "http://localhost:19530"

embeddings_model = OllamaEmbeddings(model="llama3")

vector_store = Milvus(
    embedding_function=embeddings_model,
    connection_args={"uri": URI},
    index_params={"index_type": "FLAT", "metric_type": "L2"},
)

def main():
    print("This is the main function of the Ollama3 Embedding module.")

    file_path = '/Users/zachkennedy/Dev/langchain-rag/backend/rag_pipeline/doc_handler/FS_Golfers_Guide_1.pdf'

    docs = pdf_loader.pdf_loader(file_path)
    # split_docs = splitter.split_text(docs)

    stored_ids = []
    for doc in docs:
        print(f"Embedding and storing document {len(stored_ids) + 1} out of {len(docs)}...")
        embedding = embeddings_model.embed_documents([doc.page_content])
        embedding_id = vector_store.add_embeddings(
            texts=[doc.page_content],
            embeddings=embedding,
            metadatas=[doc.metadata],
            ids=[f'{uuid.uuid4()}']
        )
        stored_ids.append(embedding_id[0])

    print(f"Stored {len(stored_ids)} documents in the vector store: ",stored_ids)





if __name__ == "__main__":
    main()