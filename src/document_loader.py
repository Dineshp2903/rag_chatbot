from abc import ABC,abstractmethod
from constant import PDF_FILE_PATH
from langchain_community.document_loaders import PyPDFLoader
import os
from vectordb import VectorDB
from functools import lru_cache
from llmexecutor import Groq
from prompt import ChatGroqPrompt



class DocumentLoader(ABC):
    @abstractmethod
    def load(self,source:str):
        pass


class PDFLoader(DocumentLoader):
    
    @lru_cache(maxsize=128)
    def load(self,source:str):
        try:
            # Load all the files in the pdf directory
            print("Loading files")

            list_of_links = [os.path.join(PDF_FILE_PATH, file) for file in os.listdir(PDF_FILE_PATH) if os.path.isfile(os.path.join(PDF_FILE_PATH, file))]

            pages = []
            for link in list_of_links:
                loader = PyPDFLoader(link)
                pages.extend(loader.load_and_split())
            print("Loaded successfully")
            return pages
        except Exception as e:
            return f"Error getting files: {e}"
