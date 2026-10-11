from shipping import calculate_shipping

def test_free_shipping():
    assert calculate_shipping(100) == 0

def test_standed_shipping():
    assert calculate_shipping(75) == 5

def test_below_order_shipping():
    assert calculate_shipping(25) == 10

def test_fifty_dollar_boundary():
    assert calculate_shipping(50) == 5

def test_just_below_free_shipping():
    assert calculate_shipping(99.99) == 5