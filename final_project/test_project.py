# unit tests for project.py
from project import *


def test_comp_choice():
    assert comp_choice() != "cat"
    assert comp_choice() != "dog"


def test_get_bid():
    assert get_bid != 5
    assert get_bid != 25
    assert get_bid != "cat"
    

def test_get_result():
    assert get_result("rock", "paper") == "computer wins"
    assert get_result("paper", "scissor") == "computer wins"
    assert get_result("paper", "paper") == "it's a tie"
    
    
def test_calculate_balance():
    assert calculate_balance("player wins", 10, 100, 100) == (110, 90)
    assert calculate_balance("computer wins", 30, 100, 100) == (70, 130)
    
    
def test_get_end_result():
    assert get_end_result(110, 90) == "player won the game"
    assert get_end_result(70, 130) == "computer won the game"
    assert get_end_result(100, 100) == "it's a tie, you should play again"