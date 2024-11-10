from plates import is_valid


def test_str_length():
    assert is_valid("AB1234") == True
    assert is_valid("AB12") == True
    assert is_valid("A") == False
    
    
def test_first_two_letters():
    assert is_valid("FGF1") == True
    assert is_valid("12345") == False
    
    
def test_all_alphanumeric():
    assert is_valid("ABC123") == True
    assert is_valid("AB./!") == False


def test_number_after_number():
    assert is_valid("AB1F1") == False
    assert is_valid("AB120") == True
    

def test_first_num_not_zero():
    assert is_valid("AB0123") == False
    assert is_valid("AB1012") == True
    
    
def test_case_insensitive():
    assert is_valid("abc123") == True
