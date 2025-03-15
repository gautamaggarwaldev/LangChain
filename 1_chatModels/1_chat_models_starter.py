from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result = llm.invoke("What is the square root of 49?")

print(result.content)