
from document_loader import PDFLoader
from constant import PDF_FILE_PATH
from vectordb import VectorDB
from llmexecutor import Groq
from prompt import ChatGroqPrompt

if __name__ == "__main__":
    loader = PDFLoader()
    pages = loader.load(PDF_FILE_PATH) 
    #print(pages)
    # vectorDb = VectorDB().add(pages)
    retriever = VectorDB().add(pages).get_retriver()
    llm = Groq().execute()
    print(ChatGroqPrompt().ask(retriever,llm,"What are the data types in java"))