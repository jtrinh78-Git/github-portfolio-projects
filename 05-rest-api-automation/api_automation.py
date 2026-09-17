import requests

url = "https://jsonplaceholder.typicode.com/posts"
update_url = "https://jsonplaceholder.typicode.com/posts/1"

post_data = {
    "title": "learn APIs",
    "body": "Practicing POST requests",
    "userId": 1,
}

update_data = {
    "title": "API practice",
}

action = input("Choose POST, PUT, or DELETE: ")

if action == "POST":
    response = requests.post(url, json=post_data)
    print(response.status_code)
    print(response.json())

elif action == "PUT":
    update_response = requests.put(update_url, json=update_data)
    print(update_response.status_code)
    print(update_response.json())

elif action == "DELETE":
    delete_response = requests.delete(update_url)
    print(delete_response.status_code)
    print(delete_response.json())

else:
    print("Invalid choice")