from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# create a gemini_nai model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a facts expert who knows about {animal}."),
    ("human", "Tell me {fact_count} facts."),
])

# Create the combined chain using Langchain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

# chain = prompt_template | model
# content='1. Tigers are the largest living cat species.  While Siberian tigers are generally the largest subspecies, Bengal tigers 
# are the most numerous.\n2.  No two tigers have the same stripe pattern.  Like human fingerprints, these stripes are unique identifiers.\n3. 
# Tigers are incredibly strong swimmers. Unlike many other cats, they actually enjoy water and often cool off in lakes or rivers, and can even 
# swim several miles.' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 
# 'STOP', 'safety_ratings': []} id='run-2b1d3dc3-d21b-4539-a220-898b583ccc58-0' usage_metadata={'input_tokens': 16, 'output_tokens': 86, 
# 'total_tokens': 102, 'input_token_details': {'cache_read': 0}}

# Run the chain
result = chain.invoke({"animal":"Tiger", "fact_count": 3})

print(result)   