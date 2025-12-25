import os
from dotenv import load_dotenv
from loguru import logger
from langchain_openai import ChatOpenAI 
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()

if os.environ["OPENAI_API_KEY"]:
    logger.info(f'API Key is set')

def train_model():
    logger.info(f'Extracting text from PDF')
    pdf_path='./Company_pdf/Localhost_404_Ltd.pdf'
    loader=PyPDFLoader(pdf_path)
    docs=loader.load()
    logger.info(f'Done with PDF text extraction')

    logger.info(f'Creating own metadata for the documents')
    for each_data_block in docs:
        each_data_block.metadata={'source':'Localhost_404_Ltd.pdf',
                    'developer':'Gemeni_dumpy_data'}
    logger.info(f'Done with metadata creation')
    


    splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=10)

    chunks=splitter.split_documents(docs)

    embeddings_model=OpenAIEmbeddings(model="text-embedding-3-small")

    vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings_model,
    persist_directory='./CompanyDB/'
    )

    #return vectorstore




if __name__ == "__main__":
    logger.info("Running train model")
    train_model()
    logger.info('Complete training')