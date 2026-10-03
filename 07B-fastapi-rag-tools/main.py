# SECTION 1 — IMPORTS
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import math
import json
from dotenv import load_dotenv

# SECTION 2 — APP AND OPENAI SETUP
load_dotenv()
client = OpenAI()
app = FastAPI()

# SECTION 3 — DOCUMENTS
documents = [
    "Bearded dragons make great pets.",
    "Coffee is great in the morning to get some caffeine in.",
    "The earth is round from space."
]

# SECTION 4 — COSINE SIMILARITY FUNCTION
def cosine_similarity(a,b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (magnitude_a * magnitude_b)

# SECTION 5 — DOCUMENT EMBEDDINGS
document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)
document_vectors = [item.embedding for item in document_response.data]

# SECTION 6 — PYTHON TOOL FUNCTION
def calculate(a,b):
    return a + b

# SECTION 7 — TOOL SCHEMA
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
            "required": ["a", "b"]
        }
    }
]

# SECTION 8 — REQUEST MODEL
class QuestionRequest(BaseModel):
    question: str

# SECTION 9 — POST /ask ENDPOINT
@app.post("/ask")
async def ask(request: QuestionRequest):
    # SECTION 10 — QUERY EMBEDDING
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=request.question
    )
    query_vector = query_response.data[0].embedding

    # SECTION 11 — SIMILARITY SEARCH
    scores = []

    for document_vector in document_vectors:
        score = cosine_similarity(query_vector, document_vector)
        scores.append(score)

    # SECTION 12 — BEST DOCUMENT RETRIEVAL
    best_index = scores.index(max(scores))
    best_document = documents[best_index]

    # SECTION 13 — AUGMENTED RAG PROMPT
    augmented_prompt = f"""
    Context: {best_document}
    Question: {request.question}
    Answer using context"""

    # SECTION 14 — FIRST LLM RESPONSE
    response= client.responses.create(
        model="gpt-5.4-mini",
        input=augmented_prompt,
        tools=tools
    )

    # SECTION 15 — TOOL CALL DETECTION
    for item in response.output:
        if item.type == "function_call":
            if item.name == "calculate":
                # SECTION 16 — TOOL ARGUMENT PARSING AND EXECUTION
                args = json.loads(item.arguments)
                result = calculate(args["a"], args["b"])
                # SECTION 17 — TOOL RESULT RETURNED TO LLM
                tool_outputs = []
                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(result)
                })
                # SECTION 18 — FINAL AI RESPONSE
                final_response = client.responses.create(
                    model="gpt-5.4-mini",
                    previous_response_id=response.id,
                    input=tool_outputs
                )
                # SECTION 19 — API JSON RESPONSE
                return {"answer": final_response.output_text}
    return {"answer": response.output_text}