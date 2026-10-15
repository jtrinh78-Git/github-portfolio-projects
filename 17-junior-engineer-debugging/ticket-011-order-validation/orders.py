def can_place_order(customer, price):
    has_enough_money = customer["balance"] >= price
    is_active = customer["status"] == "active"

    return has_enough_money and is_active


customer = {
    "name": "Sarah",
    "balance": 500,
    "status": "active"
}

result = can_place_order(customer, 200)

print(result)