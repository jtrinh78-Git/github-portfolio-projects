# Section 1 — Imports

from discount import calculate_total


# Section 2 — Test Discount Calculation

def test_calculate_total():
    result = calculate_total(100, 20)
    assert result == 80

# Section 3 - Test Another Discount

def test_calculate_total_second():
    result = calculate_total(200, 10)
    assert  result == 180