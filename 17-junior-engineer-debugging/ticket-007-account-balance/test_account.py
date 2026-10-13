# section 1 -

from account import account, deposit

# section 2 - 

def test_deposit():
    account["balance"] = 200
    result = deposit(75)

    assert result == 275
    