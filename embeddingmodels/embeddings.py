from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    
    model = 'text-embeddings-3-large',
    dimensions=64
)

text = [
    "What is the Python?",
    "Why are used the Python?",
]


vector = embeddings.aembed_documents(text)

print(vector)