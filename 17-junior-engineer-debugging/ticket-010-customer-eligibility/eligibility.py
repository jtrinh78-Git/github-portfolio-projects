def is_premium_customer(customer):
    return customer["balance"] >= 500

customer = {
    "name": "Sarah",
    "balance": 750
}

result = is_premium_customer(customer)

print(result)