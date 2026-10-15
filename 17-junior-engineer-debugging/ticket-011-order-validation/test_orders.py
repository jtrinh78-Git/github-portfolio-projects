from orders import can_place_order

def test_inactive_customer_cannot_place_order():
    customer = {
        "name": "John",
        "balance": 500,
        "status": "inactive"
    }

    result = can_place_order(customer, 200)

    assert result == False


def test_active_customer_with_enough_money_can_place_order():

    customer = {
        "name": "Sarah",
        "balance": 500,
        "status": "active"
    }

    result = can_place_order(customer, 200)

    assert result == True


def test_active_customer_without_enough_money_cannot_place_order():

    customer = {
        "name": "Mike",
        "balance": 100,
        "status": "active"
    }

    result = can_place_order(customer, 200)

    assert result == False