def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


cart = [20, 50, 80]

print(calculate_total(cart))