from langchain_ollama import OllamaEmbeddings



import pdf_loader
import splitter




embeddings_model = OllamaEmbeddings(model="llama3")

def main():
    print("This is the main function of the Hugging Face Embedding module.")

    file_path = '/Users/zachkennedy/Dev/langchain-rag/backend/rag_pipeline/doc_handler/FS_Golfers_Guide_1.pdf'

    docs = pdf_loader.pdf_loader(file_path)
    split_docs = splitter.split_text(docs)

    for doc in split_docs:
        embedding = embeddings_model.embed_documents([doc.page_content])
        print(f"Document page {doc.metadata['page']} embedding: {embedding}")

        # Should store the embeddings and doc metadata in a database or vector store
        # break




if __name__ == "__main__":
    main()