from twttr import shorten


def test_lowercase():
    assert shorten("kutya") == "kty"
    assert shorten("zsombi") == "zsmb"
    
    
def test_uppercase():
    assert shorten("KUTYA") == "KTY"
    assert shorten("ZSOMBI") == "ZSMB"
    
    
def test_numbers():
    assert shorten("kutya123") == "kty123"
    
    
def test_punctuation():
    assert shorten("..zsombi..") == "..zsmb.."

