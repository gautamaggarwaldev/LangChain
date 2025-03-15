from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage("Solve the following Math problem"),
    HumanMessage("What is the cube root of 7489?"),
]

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = model.invoke(messages)
print(f"Answer from Google Generative AI: {result.content}")

m = ChatDeepSeek(model="deepseek/deepseek-r1:free")
result = m.invoke(messages)
print(f"Answer from DeepSeek: {result.content}")