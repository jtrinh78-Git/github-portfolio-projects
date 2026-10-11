from discount import calculate_discount

def test_twenty_percent_discount():
    assert calculate_discount(100, 20) == 80.0

def test_zero_percent_discount():
    assert calculate_discount(200, 0) == 200.0
    