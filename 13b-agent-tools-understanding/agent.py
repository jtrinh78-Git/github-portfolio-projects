# SECTION 1 - IMPORTS
from openai import OpenAI
from dotenv import load_dotenv 
import json

# SECTION 2 - SETUP / CLIENT
load_dotenv()
client = OpenAI() 

# SECTION 3 - PYTHON TOOLS
def calculate(a, b):
    return a + b

# SECTION 4 - TOOL SCHEMAS
tools = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Add two number together",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number"
                },
                "b": {
                    "type": "number"
                }
            },
            "required": ["a", "b"]
        }
    }
]

# SECTION 5 - USER REQUEST - LLM
response = client.responses.create(
    model="gpt-5.4-mini",
    input="What is 25 + 18?",
    tools=tools
)

# SECTION 6 - LLM TOOL DECISION
tool_call = response.output[0]
print(tool_call)

# SECTION 7 - PYTHON EXECUTES TOOL
arguments = json.loads(tool_call.arguments)
print(arguments)
result = calculate(**arguments)
print("Tool result:", result)

# SECTION 8 - TOOL RESULT - LLM
tool_output = {
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
}
final_response = client.responses.create(
    model="gpt-5.4-mini",
    previous_response_id=response.id,
    input=[tool_output]
)

# SECTION 9 - FINAL ANSWER.  
print(final_response.output_text)
