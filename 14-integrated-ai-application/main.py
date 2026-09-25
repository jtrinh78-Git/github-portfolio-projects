# SECTION 1 — IMPORTS

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3
import math
import json


# SECTION 2 — SETUP / CLIENT

load_dotenv()

client = OpenAI()


# SECTION 3 — DATABASE

conn = sqlite3.connect("customers.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

conn.commit()


# SECTION 4 — KNOWLEDGE / RAG DATA

knowledge = [
    "Premium customers receive priority support.",
    "Customers can update their email address through account settings.",
    "Customers can view their account balance at any time.",
]


# SECTION 5 — EMBEDDINGS + VECTOR SEARCH

knowledge_vectors = []

for text in knowledge:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    vector = response.data[0].embedding
    knowledge_vectors.append(vector)


def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    return dot_product / (magnitude_a * magnitude_b)


def search_knowledge(question):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )

    question_vector = response.data[0].embedding

    scores = []

    for vector in knowledge_vectors:
        score = cosine_similarity(question_vector, vector)
        scores.append(score)

    best_index = scores.index(max(scores))

    return knowledge[best_index]


# SECTION 6 — PYTHON TOOL

def get_customer(customer_id):
    cursor.execute(
        "SELECT * FROM customers WHERE id = ?",
        (customer_id,)
    )

    customer = cursor.fetchone()

    if customer:
        return {
            "id": customer[0],
            "name": customer[1],
            "email": customer[2]
        }

    return {"error": "Customer not found"}


# SECTION 7 — TOOL SCHEMA

tools = [
    {
        "type": "function",
        "name": "get_customer",
        "description": "Get a customer from the database by ID",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer"
                }
            },
            "required": ["customer_id"]
        }
    }
]


# SECTION 8 — FASTAPI REQUEST MODEL

class Question(BaseModel):
    question: str


# SECTION 9 — API ENDPOINT

app = FastAPI()


@app.post("/ask")
def ask(data: Question):

    # SECTION 10 — RETRIEVE RELEVANT KNOWLEDGE

    relevant_knowledge = search_knowledge(data.question)


    # SECTION 11 — USER REQUEST → LLM

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=f"Question: {data.question}\nRelevant knowledge: {relevant_knowledge}",
        tools=tools
    )


    # SECTION 12 — LLM TOOL DECISION

    tool_call = response.output[0]

    if tool_call.type == "function_call":


        # SECTION 13 — PYTHON EXECUTES TOOL

        arguments = json.loads(tool_call.arguments)

        result = get_customer(**arguments)


        # SECTION 14 — TOOL RESULT → LLM
        tool_output = {
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(result)

        }
        final_response = client.responses.create(
            model="gpt-5.4-mini",
            previous_response_id=response.id,
            input=[tool_output]
        )
        return {"answer": final_response.output_text}

    # SECTION 15 — FINAL API RESPONSE
    return {"answer": response.output_text}
