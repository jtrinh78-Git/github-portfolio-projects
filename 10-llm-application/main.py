from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

previous_response_id = None

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=user_message,
            previous_response_id=previous_response_id

        )
        previous_response_id = response.id
        print(response.output_text)
    except Exception as error:
        print("Error:", error)
