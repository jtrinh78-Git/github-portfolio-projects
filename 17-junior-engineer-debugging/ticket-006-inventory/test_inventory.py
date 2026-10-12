# section 1 - import

from inventory import inventory, purchase_item


# section 2 - test succesful purchase

def test_succesful_purchase():
    inventory["laptops"] = 10

    result = purchase_item("laptops", 2)

    assert result == 8
    assert inventory["laptops"] == 8

# section 3 - test insufficient stock

def test_insufficient_stock():
    inventory["laptops"] = 10

    result = purchase_item("laptops", 15)

    assert result == "Not enough stock"
    assert inventory["laptops"] == 10

# section 4 - test unknown product

def test_unknown_product():
    result = purchase_item("phones", 2)

    assert result == "Item not found"

# section 5 - test negative quantity

def test_negative_quantity():
    inventory["laptops"] = 10

    result = purchase_item("laptops", -3)

    assert result == "Invalid quantity"
    assert inventory["laptops"] == 10

def test_zero_quantity():
    inventory["laptops"] = 10

    result = purchase_item("laptops", 0)

    assert result == "Invalid quantity"
    assert inventory["laptops"] == 10