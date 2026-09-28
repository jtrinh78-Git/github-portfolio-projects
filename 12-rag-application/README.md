# RAG Application

A Python application that demonstrates Retrieval-Augmented Generation (RAG) using OpenAI embeddings, cosine similarity, semantic search, and an LLM-generated response.

## How It Works

1. Stores a small collection of documents.
2. Converts the documents into embeddings.
3. Converts the user's question into an embedding.
4. Uses cosine similarity to compare the question with each document.
5. Retrieves the most relevant document.
6. Adds the retrieved document to the user's question as context.
7. Sends the augmented prompt to an LLM.
8. Generates an answer using the retrieved context.

## Technologies

- Python
- OpenAI API
- OpenAI Embeddings
- Retrieval-Augmented Generation (RAG)
- Cosine Similarity
- Semantic Search
- python-dotenv

## Example

```text
Ask a question: What animal makes a good pet?
Retrieved document: Dogs are loyal and friendly animals.
A dog makes a good pet.
```

## Setup

Install the required packages:

```bash
pip install openai python-dotenv
```

Create a `.env` file and add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
python3 rag.py
```

## Security

API keys are stored in a `.env` file and excluded from Git using `.gitignore`.