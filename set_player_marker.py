# Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.
'''
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
'''


# code-review:
def player_input_2():
    while True: # nie ma porzeby sprwadzać ==,  while choice
        player1 = input("Player 1: please pick a marker 'X' or 'O'\n")
        if player1 == 'X':
            player2 = 'O'
            return player1, player2
        elif player1 == 'O':
            player2 = 'X'
            return player1, player2
    


players = player_input_2()

print(players[0])