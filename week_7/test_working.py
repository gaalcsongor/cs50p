import pytest
from working import convert


def test_conversion():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    

def test_range():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM") == ValueError
        assert convert("9 AM to 16 PM") == ValueError
    