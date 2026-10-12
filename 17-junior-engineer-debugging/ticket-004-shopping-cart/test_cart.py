from cart import calculate_total


def test_calculate_total():
    assert calculate_total([20, 50, 80]) == 150

def test_empty_cart():
    assert calculate_total([]) == 0