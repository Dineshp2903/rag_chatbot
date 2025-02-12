from abc import ABC,abstractmethod
from langchain_core.prompts import PromptTemplate

class Prompt(ABC):
    @abstractmethod
    def ask(self, question: str) -> str:
        pass


class ChatGroqPrompt(Prompt):
    def ask(self, retriver,llm,question):
        prompt_extract = PromptTemplate.from_template(
                                    """
                                    ### SCRAPED TEXT FROM Book
                                    {page_data}
                                    ### INSTRUCTION
                                    The Scraped text is from the the book
                                    Don't create own link. Just share the page link provided in the input
                                    Your job is to extract the {match} details,link and return the result in JSON Object format key is question and answer in value
                                    ### OUTPUT FORMAT
                                    return type JSON
                                    ### JSON
                                    """
                                )
        chain_extract = prompt_extract | llm
        rag = retriver.invoke(question)
        res = chain_extract.invoke(input = {"page_data": rag[0].page_content,"match":question})
        print(res.content)
        return res.content
        