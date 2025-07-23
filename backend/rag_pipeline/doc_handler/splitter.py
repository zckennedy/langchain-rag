from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document
from pdf_loader import pdf_loader

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

'''Splits document further into smaller chunks for processing. Should seperate paragraphs or sections.'''

def split_text(docs):
    print("Splitting documents into smaller chunks...")

    split_docs = text_splitter.transform_documents(docs)
    print(f"Split into {len(split_docs)} chunks.")
        
    return split_docs

def main():
    print("This is the main function of the text splitter module.")

    file_path = '/Users/zachkennedy/Dev/langchain-rag/backend/rag_pipeline/doc_handler/FS_Golfers_Guide_1.pdf'

    docs = pdf_loader(file_path)
    split_docs = split_text(docs)

    with open("./PDF_Split.txt", "w") as f:
        i = 0 
        for doc in split_docs:
            f.write(f"Document page {doc.metadata['page']} - {i}: " + doc.page_content)
            i += 1
    


if __name__ == "__main__":
    main()