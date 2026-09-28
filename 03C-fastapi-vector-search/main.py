# SECTION 1 - IMPORTS
from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# SECTION 2 — SETUP / CLIENT
load_dotenv()
client = OpenAI()

# SECTION 3 - FASTAPI APP
app = FastAPI()

# SECTION 4 - DOCUMENT DATA
documents = [
    "Dogs are loyal and friendly animals.",
    "Python is a popular programming language.",
    "Saturn is a planet with rings."
]

# SECTION 5 - COSINE SIMILARITY
def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a * a for a in vector_a) ** 0.5
    magnitude_b = sum(b * b for b in vector_b) ** 0.5
    return dot_product / (magnitude_a * magnitude_b)

# SECTION 6 - DOCUMENT EMBEDDINGS
document_vectors = []
for document in documents:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=document
    )
    document_vector = response.data[0].embedding
    document_vectors.append(document_vector)

# SECTION 7 - REQUEST MODEL
class SearchRequest(BaseModel):
    query: str

# SECTION 8 - SEARCH ENDPOINT
@app.post("/search")
def search(request: SearchRequest):

        #SECTION 9 - QUERY EMBEDDING
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=request.query
    )
    query_vector = query_response.data[0].embedding

        # SECTION 10 - VECTOR COMPARISON
    scores = []
    for document_vector in document_vectors:
        score = cosine_similarity(query_vector, document_vector)
        scores.append(score)

        # SECTION 11 - BEST MATCH
    best_score = max(scores)
    best_index = scores.index(best_score)
    best_document = documents[best_index]

        # SECTION 12 - JSON RESPONSE
    return {
        "query": request.query,
        "best_match": best_document,
        "similarity": best_score
    }
