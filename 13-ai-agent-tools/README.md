# AI Agent + Tools

A Python AI agent that uses the OpenAI Responses API to select and execute tools based on a user's request.

## Features

- Uses an LLM to decide which tool to call
- Defines multiple Python tools
- Uses structured function calling
- Parses tool arguments from JSON
- Executes the selected Python function
- Returns tool results to the LLM
- Generates a final natural-language response

## Tools

### Calculator
Adds two numbers together.

### Word Length
Counts the number of characters in a word.

## Agent Workflow

1. The user sends a request.
2. The LLM determines which tool should handle the request.
3. The LLM returns a function call with structured arguments.
4. Python parses the arguments.
5. Python executes the selected tool.
6. The tool result is sent back to the LLM.
7. The LLM generates the final response.

## Architecture

User Request  
→ LLM Tool Decision  
→ Function Call  
→ Python Tool Execution  
→ Tool Result  
→ LLM Final Response

## Technologies

- Python
- OpenAI Responses API
- Function Calling / Tools
- JSON
- python-dotenv

## Security

The OpenAI API key is stored in a local `.env` file and is not committed to Git.