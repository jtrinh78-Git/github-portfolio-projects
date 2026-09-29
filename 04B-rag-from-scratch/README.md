# RAG From Scratch

A small Retrieval-Augmented Generation (RAG) application built with Python and the OpenAI API.

## What It Does

1. Stores a small collection of documents.
2. Converts the documents into embedding vectors.
3. Converts a user question into an embedding vector.
4. Uses cosine similarity to compare the question with the documents.
5. Retrieves the most relevant document.
6. Adds the retrieved document to the LLM prompt as context.
7. Generates a natural-language answer using the retrieved context.

## Concepts Practiced

- Python functions
- Lists and loops
- List comprehensions
- Embeddings
- Vectors
- Dot products
- Vector magnitude
- Cosine similarity
- Semantic search
- Retrieval
- RAG
- OpenAI Responses API

## Architecture

Question
→ Question Embedding
→ Vector Comparison
→ Cosine Similarity
→ Best Document
→ Retrieved Context
→ LLM
→ Generated Answer