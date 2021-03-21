# Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.

def player_input():
    choice = False

    while choice == False:
        player1 = input("Player 1: please pick a marker 'X' or 'O'\n")
        if player1 == str('X') or player1 == str('O'):
            choice = True
        else:
            choice = False
            
    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'
    return player1, player2

player_input()