"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:


checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
How it is used: The concepts in this task will help you when iterating data types. They can also be used in game algorithms, allowing you to know how to check results.

Precondition: There is either one winner or a draw. len(game_result) == 3 all(len(row) == 3 for row in game_result)
"""



# Solution #1

import numpy as np

def checkio(table:list) -> str:
    matrix = []
    for i in table:
        matrix.append(' '.join(i).split())
    matrix = np.array(matrix)
    # monitor rows
    for i in range(3):
        if list(matrix[i,:]).count('X') == 3:
            return 'X'
        elif list(matrix[i,:]).count('O') == 3:
            return 'O'
    # monitor columns
    for i in range(3):
        if list(matrix[:,i]).count('X') == 3:
            return 'X'
        elif list(matrix[:,i]).count('O') == 3:
            return 'O'
    for i in range(2):
        matrix = np.fliplr(matrix)
        if list(matrix.diagonal()).count('X') == 3:
            return 'X'
        elif list(matrix.diagonal()).count('O') == 3:
            return 'O'
    return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    



    
 # Solution #2
 
def checkio(table:list) -> str:
    game = list(map(tuple, table)) # get tuple of rows
    game += tuple(zip(*game)) # get tuple of columns , unpack list with * to zip columns
    game += tuple([game[i][i] for i in (0, 1, 2)]),
    game += tuple([game[i][2-i] for i in (0, 1, 2)]),
    print(game)
    if ('X','X', 'X') in game:
        return 'X'
    elif ('O','O','O') in game:
        return 'O'
    return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
 
    
  