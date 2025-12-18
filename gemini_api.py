import os
from langchain_google_genai import ChatGoogleGenerativeAI

class CustomGeminiAPI:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Gemini API key is missing")

        os.environ["GOOGLE_API_KEY"] = api_key

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3
        )

    def generate(self, query: str) -> str:
        response = self.llm.invoke(query)
        return response.content
