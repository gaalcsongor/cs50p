# A SIMPLE GAME OF ROCK, PAPER, AND SCISSORS IN PYTHON
#### Video Demo:  <https://youtu.be/4z29yXWwQFQ>
#### Description:

My project is a game which lets the user play rock, paper, and scissors with the computer.

My project is a game which lets the user play rock, paper, and scissors with the computer.

This version is called “simple” because it doesn’t have any GUI, it communicates with the user through console commands. I’m working on a version which has a user interface as well implemented with the use of Tkinter. 

Both player and computer start with an account of 100$, and the game ends automatically if one of the accounts reaches 0$, or if the player doesn’t choose to continue the game. In the latter case the higher account wins the game. 

The game has 6x different functions, all concentrate on a different goal, and are called within main(). This way parts of the code which serve the same purpose are encapsulated within the same function, and are easier to read and more logical to follow. 

The game is played in rounds. At the start of every round the user is prompted two times. First to choose between rock, paper, and scissors, and second to make a bid. Every prompt is initiated with the use of a different function. I am using while loops in order to reprompt the user if the original input is not correct. Also prompts and return values in case of these functions are strings, which are treated case-insensitively to mitigate possible errors. 

The bid the player choose is added to the winners account and subtracted from the account of the looser at the end of each round. As it is a game of random possibilities there can be a high number of rounds, therefore if have implemented an if statement at the end of the main() function where the player can decide to play another round or not. If the user decides to play another round, the actual state of the accounts are displayed before he is prompted again for a bid. The actual state of the accounts is calculated by the calculate_balance() function. It takes 4 arguments and returns the player and computer balance as integers. If the user chooses not to play another round, the get_end_result() function is called, which returns a string depending on which account has a higher integer value. This string is being printed at the end of the game, so the user knows who won the whole game. 

The player_choice() function uses a while loop to prompt the user for choice between rock, paper, and scissor. It accepts two types of inputs in case of all three answers by using string items in lists. It also returns a string value.

I am using the random library to implement the choice of the computer. This is done by the comp_choice() function, which randomly chooses one item from a list of strings and returns this as a value. 

The get_bid() function prompts the user for a string value with or without the use of a “$” prefix. It returns a string value without the prefix, also reprompts the user if the input is different from the ones he is allowed to choose, or if it’s not correct.

The get_result() function takes two string arguments which are the return values of player_choice() and comp_choice(). 
