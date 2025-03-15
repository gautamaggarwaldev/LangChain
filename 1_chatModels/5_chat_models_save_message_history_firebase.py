from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from dotenv import load_dotenv

# Set up firebase store
PROJECTID="langchain-9aad8"
SESSION_ID="X7pQ9zLwT2mNvR3Y"
# COLLECTION_NAME="chat_history"

# Initalize fire store client
print("Initalizing Firestore client...")
client = firestore.Client(project=PROJECTID)

# Initalize firestore chat message history
print("Initalizing Firestore chat message history...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    # collection_name=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized")
print("Current Chat History:", chat_history.messages)

# Initialize chat model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

print("Start chatting with AI. Type 'exit' to end the conversation.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")


