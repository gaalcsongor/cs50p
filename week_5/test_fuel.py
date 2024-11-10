import pytest
from fuel import convert, gauge


def test_convert_int_conversion():
    assert convert("2/3") == 67
    assert convert("4/8") == 50
    

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ValueError):
        convert("kutya/2")
        
        
def test_gauge_str_conversion():
    assert gauge(41) == "41%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

