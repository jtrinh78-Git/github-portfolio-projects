import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Status: ", response.status_code)

        data = response.json()

        search_name = input("Enter a user name: ")
        found = False

        for user in data:
            if user["name"].lower() == search_name.lower():
                found = True
                print(user["name"], user["email"], user["address"]["city"], user["address"]["geo"]["lat"], user["address"]["geo"]["lng"], user["company"]["name"])

        if found == False:
            print("User not found")
    else:
        print("Request failed", response.status_code)

except requests.exceptions.ConnectionError:
    print("Connection failed")