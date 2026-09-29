# SECTION 1 - IMPORTS
import math
from openai import OpenAI
from dotenv import load_dotenv

# SECTION 2 - SETUP / CLIENT
load_dotenv()
client = OpenAI()

# SECTION 3 - DOCUMENT DATA
documents = [
    "Humans are top of the food chain.",
    "Tesla CEO is named Elon Musk.",
    "Lions eat their prey raw."
]

# SECTION 4 - COSINE SIMILARITY
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(x * x for x in b))
    return dot_product / (magnitude_a * magnitude_b)

# SECTION 5 - DOCUMENT EMBEDDINGS
document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)
document_vectors = [
    item.embedding for item in document_response.data
]
# SECTION 6 - USER QUESTION
question = "Who is the CEO of Tesla?"
# SECTION 7 - QUESTION EMBEDDING
question_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=question
)
question_vector = question_response.data[0].embedding
# SECTION 8 - VECTOR COMPARISON
similarities = []
for document_vector in document_vectors:
    similarity = cosine_similarity(question_vector, document_vector)
    similarities.append(similarity)

# SECTION 9 - RETRIEVAL
best_index = similarities.index(max(similarities))
best_document = documents[best_index]
# SECTION 10 - RAG PROMPT / CONTEXT
prompt = f"""
Context: {best_document}

Question: {question}

Answer using the context above.
"""
# SECTION 11 - LLM RESPONSE
response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt
)

# SECTION 12 - FINAL ANSWER
answer = response.output_text
print(answer)