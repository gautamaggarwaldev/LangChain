from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# create a gemini_nai model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a facts expert who knows about {animal}."),
    ("human", "Tell me {fact_count} facts."),
])

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equvalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
res = chain.invoke({"animal":"Diceros bicornis longipes", "fact_count":3})

print(res)