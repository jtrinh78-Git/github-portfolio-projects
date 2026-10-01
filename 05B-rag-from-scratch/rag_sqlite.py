# SECTION 1 - IMPORTS
import math
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# SECTION 2 - SETUP / CLIENT
load_dotenv()
client = OpenAI()
app = FastAPI()

# SECTION 3 - DATABASE SETUP
connection = sqlite3.connect("rag.db")
cursor = connection.cursor()

# SECTION 4 - CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
    )
    """)
connection.commit()

# SECTION 5 - SEED DATABASE
cursor.execute("SELECT COUNT(*) FROM documents")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany(
        "INSERT INTO documents (content) VALUES (?)",
        [
            ("Bearded dragons are cold-blooded reptiles.",),
            ("Coffee contains caffenine.",),
            ("Apple makes Mac Computers.",)
        ]
    )
    connection.commit()

# SECTION 6 - LOAD DOCUMENTS
cursor.execute("SELECT content FROM documents")
rows = cursor.fetchall()
documents = [row[0] for row in rows]

# SECTION 7 - COSINE SIMILARITY
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (magnitude_a * magnitude_b)

# SECION 8 - DOCUMENT EMBEDDINGS
document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)
document_vectors = [
    item.embedding for item in document_response.data
]
# SECTION 9 - REQUEST MODEL
class Question(BaseModel):
    query: str

# SECTION 10 - API ENDPOINT
@app.post("/ask")
def ask_question(question: Question):
    query = question.query

# SECTION 11 - QUERY EMBEDDING
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
)
    query_vector = query_response.data[0].embedding 

    # SECTION 12 - VECTOR COMPARISON
    similarities = []
    for document_vector in document_vectors:
        similarity = cosine_similarity(
            query_vector,
            document_vector
        )
        similarities.append(similarity)
    # SECTION 13 - RETRIEVAL
    best_index = similarities.index(max(similarities))
    best_document = documents[best_index]
    # SECTION 14 - AUgmented Prompt
    prompt = f"""
    Context:
    {best_document}
    Question:
    {query}
    Answer using the context"""
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt
    )
    answer = response.output_text
    return{"answer": answer}

