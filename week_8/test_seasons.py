from seasons import convert


def test_convert():
    assert convert(123) == "one hundred twenty-three"
    assert convert(5) == "five"

