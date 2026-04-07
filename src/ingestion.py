from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_pdf(file_path: str):
    #Step 1: Load the PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    #Step 2: Initialze the Splitter

    #Step 3: Split the documents into chunks

    #return chunks