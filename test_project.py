from project import deposit,withdraw
import pytest

def test_deposit():
    assert deposit(100) == True

def test_withdraw():
    assert withdraw(10) == True

def test_over_withdraw():
    with pytest.raises(ValueError):
        withdraw(110)

def test_negative():
    with pytest.raises(ValueError):
        deposit(-100)
    with pytest.raises(ValueError):
        withdraw(-100)

