def calculate_shipping(order_total):
    if order_total >= 100:
        return 0
    elif order_total >= 50:
        return 5
    else:
        return 10


print(calculate_shipping(100))