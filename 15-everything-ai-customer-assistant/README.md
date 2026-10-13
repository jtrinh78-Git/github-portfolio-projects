# ============================================================
# PROJECT 15 - EVERYTHING AI CUSTOMER ASSISTANT
# HUMAN VERSION + WHY VERSION
# ============================================================


# section 1 - imports
# HUMAN: Go get all the tools we're going to need.
# WHY: Our app needs different libraries for math, AI, APIs, environment variables, JSON, databases, and data validation.

import math
from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv
import json
import sqlite3
from pydantic import BaseModel


# section 2 - client app
# HUMAN: Turn on the app and connect the AI.
# WHY: FastAPI runs our web application, while the OpenAI client lets our Python program communicate with the AI models.

load_dotenv()
app = FastAPI()
client = OpenAI()


# section 3 - database connection
# HUMAN: Open my customer filing cabinet.
# WHY: We need a connection to SQLite so our program can store, retrieve, update, and delete real customer information.

conn = sqlite3.connect("customer.db")


# section 4 - create customers table
# HUMAN: Make me a customer spreadsheet inside the database if one doesn't already exist.
# WHY: We need an organized place to store each customer's ID, name, email, and balance.

conn.execute("""
CREATE TABLE IF NOT EXISTS customers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
balance REAL)
""")


# section 5 - rag documents
# HUMAN: Give the AI some company knowledge.
# WHY: These documents contain information that our RAG system can search when a customer asks a question.

documents = [
    "Customers can update their email address.",
    "Refunds are processed within 5 business days.",
    "Premium customers receive priority support."
]


# section 6 - cosine similarity
# HUMAN: Later, when I give you two vectors, tell me how similar they are.
# WHY: We need a way to compare the meaning of the customer's question against the meaning of our company documents.

def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (mag_a * mag_b)


# section 7 - document embeddings
# HUMAN: Turn all my company knowledge into numbers that I can compare later.
# WHY: Computers can compare embedding vectors mathematically. Each document needs a vector before semantic search can happen.

document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

document_vectors = [
    item.embedding for item in document_response.data
]


# section 8 - add customer / sql insert
# HUMAN: If somebody gives me a name, email, and balance, I know how to INSERT that person into my database.
# WHY: This gives our application the CREATE part of CRUD.

def add_customer(name, email, balance):
    conn.execute("""
    INSERT INTO customers (name, email, balance)
    VALUES (?, ?, ?)
    """, (name, email, balance))

    conn.commit()


# section 9 - get customer / sql select
# HUMAN: Give me an ID and I'll SELECT that customer from the database.
# WHY: The application and AI tools need a way to retrieve real customer information instead of making it up.

def get_customer(id):
    cursor = conn.execute(
        "SELECT * FROM customers WHERE id = ?",
        (id,)
    )

    return cursor.fetchone()


# section 10 - update customer balance
# HUMAN: Give me a customer ID and a new balance, and I'll change that customer's balance.
# WHY: This gives our application the UPDATE part of CRUD.

def update_customer_balance(id, balance):
    conn.execute("""
    UPDATE customers SET balance = ? WHERE id = ?
    """, (balance, id))

    conn.commit()


# section 11 - delete customer
# HUMAN: Give me a customer ID and I'll remove that customer from the database.
# WHY: This gives our application the DELETE part of CRUD.

def delete_customer(id):
    conn.execute("""
    DELETE FROM customers WHERE id = ?
    """, (id,))

    conn.commit()


# section 12 - calculator python tool
# HUMAN: Give me two numbers and I'll add them together.
# WHY: This is a real Python function the AI can ask our application to execute when arithmetic is needed.

def calculate(a, b):
    return a + b


# section 13 - tool schemas
# HUMAN: Give the AI a menu explaining what tools it is allowed to ask for and what information each tool needs.
# WHY: The Python functions can do the work, but the AI needs a description of those functions before it knows how to request them.

tools = [{
    "type": "function",
    "name": "calculate",
    "description": "Add the two together",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
},
{
    # get_customer tool
    "type": "function",
    "name": "get_customer",
    "description": "Get a customer by their ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"}
        },
        "required": ["id"]
    }
}
]


# section 14 - pydantic request models
# HUMAN: Before somebody sends information into my API, tell me exactly what shape that information should have.
# WHY: Pydantic validates incoming data so our endpoints know they're receiving the expected fields and data types.

class CustomerRequest(BaseModel):
    name: str
    email: str
    balance: float


class QuestionRequest(BaseModel):
    question: str


# section 15 - create customer endpoint - fastapi
# HUMAN: Give people an internet doorway they can use to create a new customer.
# WHY: This connects an HTTP POST request to our Python add_customer function and ultimately our SQLite database.

@app.post("/customers")
async def create_customer(customer: CustomerRequest):
    add_customer(
        customer.name,
        customer.email,
        customer.balance
    )

    return {"message": "Customer created successfully."}


# section 16 - read customer endpoint
# HUMAN: Give me a customer ID through the API and I'll return that customer's information.
# WHY: This connects an HTTP GET request to our database lookup function and returns useful JSON to the caller.

@app.get("/customers/{customer_id}")
async def read_customer(customer_id: int):
    customer = get_customer(customer_id)

    if customer is None:
        return {
            "error": "Customer not found."
        }

    return {
        "id": customer[0],
        "name": customer[1],
        "email": customer[2],
        "balance": customer[3]
    }


# section 17 - post ask endpoint
# HUMAN: Open the front door where a customer can ask our AI assistant a question.
# WHY: We need to receive, validate, and extract the user's question before the RAG and AI pipeline can process it.

@app.post("/ask")
async def ask(request: QuestionRequest):
    question = request.question


    # section 18 - query embedding
    # HUMAN: Take the customer's English question and turn its meaning into numbers.
    # WHY: We need a query vector so we can mathematically compare the question against our document vectors.

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )

    query_vector = query_response.data[0].embedding


    # section 19 - similarity search
    # HUMAN: Compare the customer's question against every piece of company knowledge and give each one a score.
    # WHY: These scores tell us which document is semantically closest to what the customer is asking about.

    scores = []

    for document_vector in document_vectors:
        score = cosine_similarity(
            query_vector,
            document_vector
        )

        scores.append(score)


    # section 20 - best document retrieval
    # HUMAN: Find the highest score and use it to grab the original company document that won.
    # WHY: The vectors helped us FIND the best information, but the original document contains the actual text that we want to give the LLM.

    best_index = scores.index(max(scores))
    best_document = documents[best_index]


    # section 21 - augmented rag prompt
    # HUMAN: Put the winning company information beside the customer's question and hand both to the AI.
    # WHY: This gives the LLM relevant retrieved context instead of forcing it to answer only from its general knowledge.

    augmented_prompt = f"""
Use the following context to answer the user's question.

Context:
{best_document}

Question:
{question}
"""


    # section 22 - first llm response
    # HUMAN: AI, here's the customer's question, the useful company information we found, and the tools you may use. Tell me what you want to do.
    # WHY: The LLM can either answer from the RAG context or decide that it needs one of our real Python tools.

    response = client.responses.create(
        model="gpt-5-mini",
        input=augmented_prompt,
        tools=tools
    )


    # section 23 - tool call detection
    # HUMAN: Look through the AI's response and see whether it asked us to run a tool.
    # WHY: The LLM can REQUEST a tool, but our Python application is responsible for detecting and executing that request.

    for item in response.output:
        if item.type == "function_call":

            # HUMAN: The AI sent us tool arguments as JSON.
            # Turn them back into Python data that we can use.

            arguments = json.loads(item.arguments)


            # section 24 - calculator tool routing
            # HUMAN: If the AI asked for the calculator, send the numbers to our real Python calculator.
            # WHY: The LLM chooses the tool, but Python actually performs the operation.

            if item.name == "calculate":
                result = calculate(
                    arguments["a"],
                    arguments["b"]
                )


            # section 25 - database tool routing
            # HUMAN: If the AI asked for a customer, take the requested ID and look up the real customer in SQLite.
            # WHY: We want the AI to use actual database information instead of guessing or inventing customer data.

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
            # HUMAN: The tool finished its job. Now package the real result so we can hand it back to the AI.
            # WHY: The AI requested the tool, but it doesn't automatically know what happened after Python ran it.

            tool_output = {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps(result)
            }


            # section 27 - final llm response
            # HUMAN: Hey AI, here's the result from the tool you asked me to run. Now finish your answer.
            # WHY: This second AI call lets the model combine the conversation/context with the real tool result and turn it into a useful human response.

            final_response = client.responses.create(
                model="gpt-5-mini",
                input=[
                    *response.output,
                    tool_output
                ],
                tools=tools
            )


            # section 28 - tool path api response
            # HUMAN: The AI has the real tool result and has finished answering. Send that answer to the customer.
            # WHY: This completes the API request when a tool was required.

            return {
                "answer": final_response.output_text
            }


    # section 29 - no tool fallback response
    # HUMAN: The AI didn't need a tool, so just send its original answer back to the customer.
    # WHY: Not every question requires a calculator or database lookup. RAG context alone may already be enough.

    return {
        "answer": response.output_text
    }