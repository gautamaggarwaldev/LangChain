from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_History = [] # use to store a messages

system_message = SystemMessage(content="you are a helpful AI assistant")
chat_History.append(system_message) # add the message to the chat history

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_History.append(HumanMessage(content=query)) # add the message to the chat history

    result = model.invoke(chat_History)
    res = result.content
    chat_History.append(AIMessage(content=res)) # add the message to the chat history
    print(f"AI: {res}")


print("-----------------Chat History-----------------")
print(chat_History)