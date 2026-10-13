# section 1

def calculate_total(price, discount):
    final_price = price - (price * discount / 100)
    return final_price


total = calculate_total(200, 10)

print("Final total:", total)