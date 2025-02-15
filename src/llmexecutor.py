import getpass
import os
from abc import ABC,abstractmethod
from dotenv import load_dotenv
from langchain_groq import ChatGroq


class LLMExecutor(ABC):
    @abstractmethod
    def execute(self,source:str):
        pass

class Groq(LLMExecutor):
    def execute(self):
        load_dotenv()
        try:
            print("Loading LLM model")
            llm = ChatGroq(
                model="mixtral-8x7b-32768",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            )
            return llm
        except Exception as e:
            print(f"Error loading LLM model: {e}")
            return f"Error executing command: {e}"
