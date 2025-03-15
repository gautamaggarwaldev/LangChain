from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({
#     "tone": "energetic",
#     "company": "Google",
#     "position": "Software Engineer",
#     "skill": "Python"
# })

# result = llm.invoke(prompt)

# print(result.content)


# EXAMPLE 2: Prompt with system and human messages (using tuples)

messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me a {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({
    "topic": "engineers",
    "joke_count": 4
})

print("\n---------------PROMPT WITH SYSTEM AND HUMAN MESSAGES--------------------\n")
print(prompt)
