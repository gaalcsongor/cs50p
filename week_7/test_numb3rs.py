from numb3rs import validate


def test_range():
    assert validate("123.5.111.62") == True
    assert validate("123.5.111.256") == False
    

def test_numbers():
    assert validate("cat") == False
    assert validate("cat.dog.chicken") == False   