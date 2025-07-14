# document_loader.py
# This module is responsible for loading documents into the RAG pipeline.
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import HTMLHeaderTextSplitter, HTMLSemanticPreservingSplitter


def web_loader(source_url: str):
    print("Loading documents from the web...")

    loader = WebBaseLoader(
        web_paths=[source_url],
        show_progress=True,
        # bs_kwargs=dict(parse_only=bs4.SoupStrainer(id='bodyContent'))
    )
    docs = []
    for doc in loader.load():
        docs.append(doc)

    return docs







def main():
    print("This is the main function of the document loader module.")
    # Add your document loading logic here

    page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/"
    # page_url = "https://en.wikipedia.org/wiki/Golf"

    docs = web_loader(page_url)
    print(f"Loaded {len(docs)} documents from {page_url}")

 
    for doc in docs:
        print(f"Document content: \n{doc.page_content}...")


if __name__ == "__main__":
   main()