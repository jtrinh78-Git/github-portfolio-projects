# LLM Application

A Python command-line chatbot that connects to the OpenAI API, accepts user input, generates AI responses, and maintains conversational context across multiple messages.

## Features

- Connects Python to an LLM through the OpenAI API
- Accepts user messages from the terminal
- Generates AI responses
- Maintains multi-turn conversation context
- Allows the user to exit the chatbot
- Uses environment variables to protect the API key
- Includes basic error handling for API failures

## Technologies

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv

## How It Works

The application follows this flow:

User Input  
↓  
Python Application  
↓  
OpenAI API  
↓  
LLM  
↓  
Generated Response  
↓  
Terminal Output

The chatbot uses `previous_response_id` to connect each new request to the previous response, allowing the model to maintain conversational context across multiple messages.

## Environment Variables

The OpenAI API key is stored in a `.env` file instead of being placed directly in the Python source code.

Example:

```text
OPENAI_API_KEY=your_api_key_here