# Integrated AI Application

A FastAPI application that combines multiple AI engineering concepts into one end-to-end system.

## Features

- FastAPI REST API
- OpenAI LLM integration
- Text embeddings
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- LLM tool calling
- Python function execution
- SQLite database integration
- Environment variable protection with `.env`

## Architecture

User Question
    ↓
FastAPI
    ↓
Embedding
    ↓
Vector Search
    ↓
Relevant Knowledge
    ↓
LLM
    ↓
Tool Decision
    ↓
Python Tool
    ↓
SQLite Database
    ↓
Tool Result
    ↓
LLM
    ↓
FastAPI Response

## API Endpoint

### POST `/ask`

Accepts a user question and returns an AI-generated answer.

Example request:

```json
{
  "question": "What support do premium customers receive?"
}