# pdf_loader.py

from langchain_community.document_loaders import PDFMinerLoader


def pdf_loader(source_path: str):
    print("Loading documents from a PDF...")

    loader = PDFMinerLoader(
        source_path,
        mode='page',
    )
    
    pages = []
    for page in loader.load():
        pages.append(page)
    print(f"Loaded {len(pages)} pages from {source_path}")

    return pages




def main():
    print("This is the main function of the PDF loader module.")

    file_path = '/Users/zachkennedy/Dev/langchain-rag/backend/rag_pipeline/loaders/FS_Golfers_Guide_1.pdf'

    docs = pdf_loader(file_path)

    for doc in docs:
        print(f"Document page {doc.metadata['page']}: \n--------------\n{doc.page_content}\n")


if __name__ == "__main__":
    main()
