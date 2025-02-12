from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorDB:
    def __init__(self):
        self.embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        pass

    def add(self, pages: list):
        #embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.faiss_index = FAISS.from_documents(pages, self.embedding_function)
        return self
    
    def get_retriver(self):
        return self.faiss_index.as_retriever()
        

    def search(self, query: str):
        retriever = self.faiss_index.as_retriever()
        return  self.faiss_index.similarity_search(query, k=2)