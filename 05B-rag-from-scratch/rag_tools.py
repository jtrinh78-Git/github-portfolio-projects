import math
import json
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3
from fastapi import FastAPI

load_dotenv()
client = OpenAI()
app = FastAPI()

documents = [
    "The Earth is round from space.",
    "Apple makes Macbooks and iPhones.",
    "AI Engineering is not easy to learn."
]

def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (magnitude_a * magnitude_b)

document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)
document_vectors = [item.embedding for item in document_response.data]

query = "What company makes iPhones, and what is 25 + 18?"

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)
query_vector = query_response.data[0].embedding

similarities = []
for document_vector in document_vectors:
    similarity = cosine_similarity(
        document_vector,
        query_vector
    )
    similarities.append(similarity)

best_index = similarities.index(max(similarities))
best_document = documents[best_index]

prompt = f"""
Context:
{best_document}
Question:
{query}
"""
def calculate(a, b):
    return a + b

tools = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Add two numbers together",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required":["a", "b"]
        }   
    }
]
response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt,
    tools=tools
)
for item in response.output:
    if item.type == "function_call":
        if item.name == "calculate":
            arguments = json.loads(item.arguments)
            result = calculate(arguments["a"], arguments["b"])
            final_response = client.responses.create(
                model="gpt-5.4-mini",
                previous_response_id=response.id,
                input = [
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result)
                    }
                ]    
            )
            answer = final_response.output_text
            print(answer)

        