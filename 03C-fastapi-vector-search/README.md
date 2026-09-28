# FastAPI Vector Search

A FastAPI application that performs semantic search using OpenAI embeddings and cosine similarity.

The API accepts a natural-language query, converts it into an embedding vector, compares it against stored document vectors, and returns the most semantically similar document.

## Features

- FastAPI POST endpoint
- Pydantic request validation
- OpenAI text embeddings
- Document embedding generation
- Vector comparison
- Cosine similarity implemented in Python
- Semantic search
- Best-match retrieval
- JSON API responses

## Technologies

- Python
- FastAPI
- Pydantic
- OpenAI API
- Uvicorn
- python-dotenv

## How It Works

The application begins with a small collection of documents:

```python
documents = [
    "Dogs are loyal and friendly animals.",
    "Python is a popular programming language.",
    "Saturn is a planet with rings."
]
```

Each document is converted into an embedding vector using the OpenAI embeddings API.

When a user sends a query to the `/search` endpoint, the application:

1. Receives the query through FastAPI.
2. Validates the request with Pydantic.
3. Converts the query into an embedding vector.
4. Compares the query vector against every document vector using cosine similarity.
5. Stores the similarity scores.
6. Finds the highest similarity score.
7. Retrieves the corresponding document.
8. Returns the query, best match, and similarity score as JSON.

## Semantic Search Pipeline

```text
User Query
    ↓
POST /search
    ↓
Pydantic SearchRequest
    ↓
OpenAI Embedding
    ↓
Query Vector
    ↓
Cosine Similarity
    ↓
Document Vectors
    ↓
Similarity Scores
    ↓
Best Score
    ↓
Best Document
    ↓
JSON Response
```

## API Endpoint

### POST `/search`

Example request:

```json
{
  "query": "What animal makes a good companion?"
}
```

Example response:

```json
{
  "query": "What animal makes a good companion?",
  "best_match": "Dogs are loyal and friendly animals.",
  "similarity": 0.5433877166607498
}
```

The query does not need to contain the same words as the stored document. Embeddings allow the application to compare semantic meaning.

## Running the Project

Install the required packages:

```bash
pip install fastapi uvicorn openai python-dotenv
```

Create a `.env` file containing your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 9000
```

The API will run locally on port `9000`.

## Testing

Send a POST request with `curl`:

```bash
curl -X POST http://127.0.0.1:9000/search \
-H "Content-Type: application/json" \
-d '{"query":"What animal makes a good companion?"}'
```

The project was tested with queries targeting all three stored documents:

```text
"What animal makes a good companion?"
→ Dogs are loyal and friendly animals.

"What can I use to write software?"
→ Python is a popular programming language.

"Which world is famous for its rings?"
→ Saturn is a planet with rings.
```

## Concepts Practiced

- REST APIs
- FastAPI endpoints
- HTTP POST requests
- JSON request and response data
- Pydantic models
- Environment variables
- OpenAI embeddings
- Vector representations
- Dot products
- Vector magnitude
- Cosine similarity
- Semantic search
- Index-based retrieval
- Python loops and nested code blocks