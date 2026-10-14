from eligibility import is_premium_customer

def test_customer_below_500_is_not_premium():
    customer = {
        "name": "John",
        "balance": 499
    }

    result = is_premium_customer(customer)

    assert result == False


def test_customer_with_exactly_500_is_premium():
    customer = {
        "name": "Sarah",
        "balance": 500
    }
    result = is_premium_customer(customer)
    assert result == True


def test_customer_above_500_is_premium():
    customer = {
        "name": "Mike",
        "balance": 501
    }
    result = is_premium_customer(customer)

    assert result == True