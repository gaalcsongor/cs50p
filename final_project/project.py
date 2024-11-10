# a simple rock, paper, scissors game console version
import random

def main():
    i = 0
    player_balance = 100
    computer_balance = 100
    print("\n***** a game of rock, paper and scissors *****\n")
    
    while True:
        i += 1
        print(f"\ngame round: {i}")
        print(f"player balance: {player_balance}")
        print(f"computer balance: {computer_balance}\n")

        player = player_choice()
        comp = comp_choice()
        bid = get_bid()
        result = get_result(player, comp)
        player_balance, computer_balance = calculate_balance(result, bid, player_balance, computer_balance)

        print(f"\nplayer: {player}\n")
        print(f"computer: {comp}\n")
        print(f"{result}\n")
        
        play_again = input("play again? (y/n) ").lower()
        if play_again in ["n", "no"]:
            print(f"player balance: {player_balance}")
            print(f"computer balance: {computer_balance}")
            print(f"the final result: {get_end_result(player_balance, computer_balance)}")
            break


def player_choice():
    while True:
        user = input("rock, paper, or scissor? ").lower()
        if user in ["r", "rock"]:
            return "rock"
        elif user in ["p", "paper"]:
            return "paper"
        elif user in ["s", "scissor"]:
            return "scissor"
        else:
            print("incorrect input, try again")
            continue
    

def comp_choice():
    items = ["rock", "paper", "scissor"]    
    return random.choice(items)


def get_bid():
    while True:
        bid = input("what is your bid? (10$/20$/30$) ")
        if bid in ["10", "10$", "20", "20$", "30", "30$"]:
            return int(bid.removesuffix("$"))
        else:
            print("not a valid bid, please try again")
            continue


def get_result(player, comp):
    # 0 - tie, 1 - player wins, 2 - comp wins
    if player == "rock":
        if comp == "rock":
            return "it's a tie"
        elif comp == "paper":
            return "computer wins"
        else:
            return "player wins"
    elif player == "paper":
        if comp == "rock":
            return "player wins"
        elif comp == "paper":
            return "it's a tie"
        else:
            return "computer wins"
    elif player == "scissor":
        if comp == "rock":
            return "computer wins"
        elif comp == "paper":
            return "player wins"
        else:
            return "it's a tie"
    
    
def calculate_balance(result, bid, player_balance, comp_balance):
    if result == "player wins":
        player_balance += bid
        comp_balance -= bid
    elif result == "computer wins":
        player_balance -= bid
        comp_balance += bid
    return player_balance, comp_balance


def get_end_result(play_bal, comp_bal):
    if play_bal > comp_bal:
        return "player won the game"
    elif play_bal < comp_bal:
        return "computer won the game"
    else:
        return "it's a tie, you should play again"
        

if __name__ == "__main__":
    main()