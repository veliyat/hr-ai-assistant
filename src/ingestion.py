from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_pdf(file_path: str):
    #Step 1: Load the PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    #Step 2: Initialze the Splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )

    #Step 3: Split the documents into chunks
    chunks = text_splitter.split_documents(pages)

    return chunks