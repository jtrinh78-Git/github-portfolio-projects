# section 1 - inventory data

inventory = {
    "laptops": 10,
    "monitors": 15,
    "keyboards": 20
}

# section 2 - purchase function

def purchase_item(item, quantity):
    if quantity <= 0:
        return "Invalid quantity"
    
    if item not in inventory:
        return "Item not found"

    if quantity > inventory[item]:
        return "Not enough stock"

    inventory[item] -= quantity

    return inventory[item]

# section 3 - test purchase
if __name__ == "__main__":
    print("Stock before:", inventory["laptops"])

    result = purchase_item("laptops", 2)

    print("Stock after:", inventory["laptops"])