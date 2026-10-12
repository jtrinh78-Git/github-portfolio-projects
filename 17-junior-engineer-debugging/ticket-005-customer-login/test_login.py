# section 1 - import

from login import login


# section 2 - test successful login

def test_correct_password():
    assert login("alice", "password123") == True

# section 3 - test incorrect password

def test_wrong_password():
    assert login("alice", "wrongpassword") == False

# section 4 - test unknown username

def test_unknown_username():
    assert login("charlie", "passowrd123") == False