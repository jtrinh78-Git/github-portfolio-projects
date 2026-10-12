# SECTION 1 - CUSTOMER DATA

users = {
    "alice": "password123",
    "bob": "secure456"
}

# SECTION 2 - LOGIN FUNCTION

def login(username, password):
    if username not in users:
        return False

    if users[username] == password:
        return True

    return False

    
if __name__ == "__main__":
    print(login("alice", "password123"))
    print(login("alice", "wrongpassword"))