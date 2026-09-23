import math

from openai import OpenAI

from dotenv import load_dotenv


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))
    return dot_product / (magnitude_a * magnitude_b)


load_dotenv()

client = OpenAI()

documents = [
    "Dogs are loyal and friendly animals.",
    "Python is a popular programming language.",
    "The Earth revolves around the Sun."
]

document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

document_embeddings = []

for item in document_response.data:
    document_embeddings.append(item.embedding)

question = input("Ask a question: ")

question_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=question
)

question_embedding = question_response.data[0].embedding

similarities = []

for document_embedding in document_embeddings:
    score = cosine_similarity(question_embedding, document_embedding)
    similarities.append(score)

best_score = max(similarities)
best_index = similarities.index(best_score)
best_document = documents[best_index]
print("Retrieved document:", best_document)

# augmented

prompt = f"""
Context:
{best_document}

Question:
{question}
"""

# generation

response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt
)

print(response.output_text)