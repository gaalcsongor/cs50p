from bank import value


def test_lowercase():
    assert value("hello") == 0
    assert value("kutya") == 100
    assert value("hi") == 20


def test_uppercase():
    assert value("HELLO") == 0
    assert value("KUTYA") == 100
    assert value("HI") == 20


def test_numbers():
    assert value(5) == 100
    assert value(25) == 100
    
    
def test_white_space():
    assert value("  hello  ") == 0
    assert value("  55  ") == 100