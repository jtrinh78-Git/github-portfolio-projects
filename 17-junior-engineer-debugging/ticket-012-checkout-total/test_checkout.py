from checkout import calculate_total


def test_checkout_total():
    result = calculate_total(10, 3)

    assert result == 30


def test_checkout_single_item():
    result = calculate_total(25, 1)

    assert result == 25
