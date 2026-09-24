import json 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()



def calculate(a, b):
    return a + b

def get_word_length(word):
    return len(word)


tools = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Add two numbers together",
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
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
    "type": "function",
    "name": "get_word_length",
    "description": "Count the number of characters in a word",
    "parameters": {
        "type": "object",
        "properties": {
            "word": {
                "type": "string"
            }
        },
        "required": ["word"],
        "additionalProperties": False
    },
    "strict": True
}
]
response = client.responses.create(
    model="gpt-5.6-luna",
    input="What is 25 + 18?",
    tools=tools,
    tool_choice="required" 

)
tool_call = response.output[0]
arguments = json.loads(tool_call.arguments)
if tool_call.name == "calculate":
    result = calculate(arguments["a"], arguments["b"])

elif tool_call.name == "get_word_length":
    result = get_word_length(arguments["word"])

tool_output = {
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
}
final_response = client.responses.create(
    model="gpt-5.6-luna",
    previous_response_id=response.id,
    input=[tool_output]
)
print(final_response.output_text)
