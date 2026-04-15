from app.checker import is_even,is_odd

def test_is_even():
    assert is_even(2) == True
    assert is_even(4) == True

def test_is_odd():
    assert is_odd(3) == True
    assert is_odd(5) == True


