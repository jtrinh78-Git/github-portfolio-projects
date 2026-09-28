# SECTION 1 - IMPORTS
from openai import OpenAI
from dotenv import load_dotenv
import math

# SECTION 2 - SETUP / CLIENT
load_dotenv()
client = OpenAI()

# SECTION 3 - TEXT DATA
text = "Dogs are loyal animals."
similar_text = "puppies make great pets."
different_text = "Saturn has rings around it."

# SECTION 4 - CREATE EMBEDDINGS
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

# SECTION 5 - INSPECT VECTORS
vector = response.data[0].embedding
print(vector[:10])

# SECTION 6 - COSINE SIMILARITY
def cosine_similarity(a, b):
    dot_product = sum(
        a_value * b_value
        for a_value, b_value in zip(a, b)
    )
    magnitude_a = math.sqrt(sum(value ** 2 for value in a))
    magnitude_b = math.sqrt(sum(value ** 2 for value in b))
    return dot_product / (magnitude_a * magnitude_b)

# SECTION 7 - COMPARE MEANING

similar_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=similar_text
)
similar_vector = similar_response.data[0].embedding

different_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=different_text
)
different_vector = different_response.data[0].embedding

similar_score = cosine_similarity(vector, similar_vector)

different_score = cosine_similarity(vector, different_vector)

print("Dog vs Puppy:", similar_score)
print("Dog vs Saturn:", different_score)

# Section 8 - Semantic Search

documents = [
    "Dogs are loyal and friendly animals.",
    "Python is a popular programming language.",
    "Saturn is a planet with rings."
]

document_vectors = []
for document in documents:
    document_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=document
    )
    document_vector = document_response.data[0].embedding
    document_vectors.append(document_vector)



query = "What animal makes a good companion?"
query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)
query_vector = query_response.data[0].embedding

scores = []
for document_vector in document_vectors:
    score = cosine_similarity(query_vector, document_vector)
    scores.append(score)

best_score = max(scores)
best_index = scores.index(best_score)
best_document = documents[best_index]
print("Query:",query)
print("Best match:", best_document)
print("Similarty:", best_score)

