import math
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

documents = [
    "Dogs are loyal and friendly animals.",
    "Python is a popular programming language.",
    "The stock market fell today."
]

documents_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

document_embeddings = []

for item in documents_response.data:
    document_embeddings.append(item.embedding)

query = "What animal makes a good pet?"

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)

query_embedding = query_response.data[0].embedding

similarities = []

for document_embedding in document_embeddings:
    dot_product = sum(
        q * d for q, d in zip(query_embedding, document_embedding)
    )

    magnitude_query = math.sqrt(sum(q * q for q in query_embedding))
    magnitude_document = math.sqrt(
        sum(d * d for d in document_embedding)
    )

    similarity = dot_product / (
        magnitude_query * magnitude_document
    )

    similarities.append(similarity)

best_index = similarities.index(max(similarities))
best_document = documents[best_index]

print("Query:", query)
print("Best match:", best_document)
print("Similarity:", max(similarities))