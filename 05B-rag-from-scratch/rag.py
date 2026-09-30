import math
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

documents = [
    "Cats are loving pets",
    "Robots are going to be the future",
    "Bearded dragons are reptiles"
]
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))
    return dot_product / (magnitude_a * magnitude_b)

# SECTION 5 - DOCUMENT EMBEDDINGS
document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)
document_vectors = [
    item.embedding for item in document_response.data
]

# SECTION 6 - USER QUERY
query_question = "Cats make a perfect pet for a family"

# SECTION 7 - QUERY EMBEDDING
query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query_question
)
query_vector = query_response.data[0].embedding

# SECTION 8 - VECTOR COMPARISON

similarities = []

for document_vector in document_vectors:
    similarity = cosine_similarity(
        query_vector,
        document_vector
    )

    similarities.append(similarity)

# SECTION 9 - RETRIEVAL
best_index = similarities.index(max(similarities))
best_document = documents[best_index]

# SECTION 10 - AUGMENTED PROMPT
prompt = f"""
Context:
{best_document}

Question:
{query_question}

Answer using the context.
"""

# SECTION 11 - LLM GENERATION

response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt
)

# SECTION 12 - FINAL ANSWER

answer = response.output_text
print(answer)

