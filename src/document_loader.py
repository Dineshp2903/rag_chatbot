from abc import ABC,abstractmethod
from constant import PDF_FILE_PATH
from langchain_community.document_loaders import PyPDFLoader
import os


class DocumentLoader(ABC):
    @abstractmethod
    def load(self,source:str):
        pass


class PDFLoader(DocumentLoader):
    def load(self,source:str):
        try:
            # Load all the files in the pdf directory

            list_of_links = [os.path.join(PDF_FILE_PATH, file) for file in os.listdir(PDF_FILE_PATH) if os.path.isfile(os.path.join(PDF_FILE_PATH, file))]

            pages = []
            for link in list_of_links:
                loader = PyPDFLoader(link)
                pages.extend(loader.load_and_split())
            print("Loaded successfully")
        except Exception as e:
            return f"Error getting files: {e}"
        

if __name__ == "__main__":
    loader = PDFLoader()
    loader.load(PDF_FILE_PATH)