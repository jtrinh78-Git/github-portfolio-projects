# section 1 - customer account

account = {
    "customer": "Alice",
    "balance": 100
}


# section 2 - deposit function

def deposit(amount):
    account["balance"] += amount
    return account["balance"]


# section 3 - manual test

if __name__ == "__main__":
    print("Balance before:", account["balance"])
    print("Balance after:", deposit(50))