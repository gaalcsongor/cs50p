from um import count


def test_input_sentences():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
    
    
def test_input_words():
    assert count("um") == 1
    assert count("yummy") == 0
    

def test_incorrect_input():
    assert count("123") == 0