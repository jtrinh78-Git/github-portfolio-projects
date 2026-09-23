# Embeddings and Vector Search

A Python project demonstrating semantic search using OpenAI embeddings and cosine similarity.

## Features

- Converts text documents into embedding vectors
- Converts a search query into an embedding
- Calculates cosine similarity between vectors
- Compares a query against multiple documents
- Identifies the most semantically similar document
- Uses environment variables to protect API credentials

## Technologies

- Python
- OpenAI API
- OpenAI Embeddings
- python-dotenv
- Cosine Similarity

## How It Works

1. Store multiple text documents.
2. Convert the documents into embeddings.
3. Convert the user's query into an embedding.
4. Calculate cosine similarity between the query and each document.
5. Select the document with the highest similarity score.

## Example

Query:

`What animal makes a good pet?`

Best match:

`Dogs are loyal and friendly animals.`

## Security

The OpenAI API key is stored in a `.env` file and is not committed to Git.