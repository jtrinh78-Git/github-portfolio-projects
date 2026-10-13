
# section 1 - imports
import math
import json
import sqlite3
from pathlib import Path

from openai import OpenAI
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel


# section 2 - client app
load_dotenv()

app = FastAPI()
client = OpenAI()


# section 3 - database connection
DB_PATH = Path(__file__).resolve().parent / "customer.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


# section 4 - create customers table
with get_connection() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        balance REAL
    )
    """)


# section 5 - rag documents
documents = [
    "Customers can update their email address.",
    "Refunds are processed within 5 business days.",
    "Premium customers receive priority support."
]


# section 6 - cosine similarity
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot_product / (mag_a * mag_b)


# section 7 - document embeddings
document_vectors = None


def get_document_vectors():
    global document_vectors

    if document_vectors is None:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=documents
        )
        document_vectors = [
            item.embedding for item in response.data
        ]

    return document_vectors


# section 8 - add customer / sql insert
def add_customer(name, email, balance):
    with get_connection() as conn:
        cursor = conn.execute("""
        INSERT INTO customers (name, email, balance)
        VALUES (?, ?, ?)
        """, (name, email, balance))

        return cursor.lastrowid


# section 9 - get customer / sql select
def get_customer(id):
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM customers WHERE id = ?",
            (id,)
        )
        return cursor.fetchone()


# section 10 - update customer balance
def update_customer_balance(id, balance):
    with get_connection() as conn:
        cursor = conn.execute("""
        UPDATE customers SET balance = ? WHERE id = ?
        """, (balance, id))

        return cursor.rowcount > 0


# section 11 - delete customer
def delete_customer(id):
    with get_connection() as conn:
        cursor = conn.execute("""
        DELETE FROM customers WHERE id = ?
        """, (id,))

        return cursor.rowcount > 0


# section 12 - calculator python tool
def calculate(a, b):
    return a + b


# section 13 - tool schemas
tools = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Add two numbers together.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "get_customer",
        "description": "Get a customer by their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"}
            },
            "required": ["id"],
            "additionalProperties": False
        },
        "strict": True
    }
]


# section 14 - pydantic request models
class CustomerRequest(BaseModel):
    name: str
    email: str
    balance: float


class QuestionRequest(BaseModel):
    question: str


# section 15 - create customer endpoint - fastapi
@app.post("/customers", status_code=201)
def create_customer(customer: CustomerRequest):
    customer_id = add_customer(
        customer.name,
        customer.email,
        customer.balance
    )

    return {
        "message": "Customer created successfully.",
        "id": customer_id
    }


# section 16 - read customer endpoint
@app.get("/customers/{customer_id}")
def read_customers(customer_id: int):
    customer = get_customer(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    return {
        "id": customer[0],
        "name": customer[1],
        "email": customer[2],
        "balance": customer[3]
    }


# section 17 - post /ask endpoint
@app.post("/ask")
def ask(request: QuestionRequest):
    question = request.question

    # section 18 - query embedding
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )

    query_vector = query_response.data[0].embedding

    # section 19 - similarity search
    scores = []

    for document_vector in get_document_vectors():
        score = cosine_similarity(
            query_vector,
            document_vector
        )
        scores.append(score)

    # section 20 - best document retrieval
    best_index = scores.index(max(scores))
    best_document = documents[best_index]

    # section 21 - augmented rag prompt
    augmented_prompt = f"""
Use the following context to answer the user's question.

Context: {best_document}

Question: {question}

If the context does not contain the answer, say so.
Use tools when appropriate.
"""

    # section 22 - first llm response
    response = client.responses.create(
        model="gpt-5-mini",
        input=augmented_prompt,
        tools=tools
    )

    # section 23 - tool call detection
    conversation = [
        {
            "role": "user",
            "content": augmented_prompt
        }
    ]

    # Allow multiple rounds of tool calls, but prevent
    # an unlimited execution loop.
    for _ in range(5):
        conversation.extend(
            item.model_dump(exclude_none=True)
            for item in response.output
        )

        function_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        # section 29 - no tool fallback response
        if not function_calls:
            return {
                "answer": response.output_text
            }

        for item in function_calls:
            arguments = json.loads(item.arguments)

            # section 24 - calculator tool routing
            if item.name == "calculate":
                result = calculate(
                    arguments["a"],
                    arguments["b"]
                )

            # section 25 - database tool routing
            elif item.name == "get_customer":
                customer = get_customer(
                    arguments["id"]
                )

                if customer is None:
                    result = "Customer not found."
                else:
                    result = {
                        "id": customer[0],
                        "name": customer[1],
                        "email": customer[2],
                        "balance": customer[3]
                    }

            else:
                result = "Unknown tool."

            # section 26 - function call output
            tool_output = {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps(result)
            }

            conversation.append(tool_output)

        # section 27 - final llm response
        response = client.responses.create(
            model="gpt-5-mini",
            input=conversation,
            tools=tools
        )

        # section 28 - tool path api response
        # Handled by the no-tool return at the
        # beginning of the next loop iteration.

    raise HTTPException(
        status_code=502,
        detail="AI tool execution exceeded the allowed rounds."
    )
