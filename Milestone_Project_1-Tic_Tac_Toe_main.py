print('Welcome to Tic Tac Toe!')

# function that can print out a board. 
def display_board(board):
    return print('\n'*5 + """
    -------------\t\t\t-------------
    | {} | {} | {} |\t\t\t| 7 | 8 | 9 |
    -------------\t\t\t-------------
    | {} | {} | {} |\t\t\t| 4 | 5 | 6 |
    ------------- \t\t\t-------------
    | {} | {} | {} |\t\t\t| 1 | 2 | 3 |
    -------------\t\t\t-------------""".format(board[7],board[8],board[9],board[4],board[5], board[6], board[1], board[2], board[3]))

# function that can take in a player input and assign their marker as 'X' or 'O'. 
def player_input(): # zmiana nazwy
    while True:
        player1 = input("Player 1: please pick a marker 'X' or 'O'\n")
        if player1 == 'X':
            player2 = 'O'
            return player1, player2
        elif player1 == 'O':
            player2 = 'X'
            return player1, player2

# function that uses the random module to randomly decide which player goes first. 
import random
def choose_first():
        if random.randint(0, 1) == 1:
            return list(('Player 1', 'Player 2'))
        else:
            return list(('Player 2', 'Player 1'))


# Function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == ' '


# function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position.
def player_choice(board):
    while True:
        try:
            choice = int(input("Chose one of the free positions on the board (1-9): "))
            if choice in range(1,10) and space_check(board,choice):
                return choice
        except:
            print('Sorry, you are out of acceptable choose 1-9') 


# function that takes in the board list object, a marker ('X' or 'O'), 
# and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker
    return board


# function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    if board[7] == board[8] == board[9] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[1] == board[2] == board[3] == mark:
        return True

    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True

    elif board[7] == board[5] == board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True

    else:
        return False

# function that checks if the board is full and returns a boolean value. 
# True if full, 
# False otherwise.
def full_board_check(board):
    return ' ' not in board


# function that asks the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    while True:
        chose = input('Do you want to play again?\nType: "y" - for yes\nType: "n" - for no\n')
        if chose == 'y':
            return True 
        elif chose == 'n':
            return False


#                   GAME            

game_on = True
while game_on == True:
    board = ['O',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    players = player_input()
    first = choose_first()
    print('Player 1 is: {} \nPlayer 2 is: {}'.format(players[0],players[1]))
    print(first[0] + ' is the first to play')
    # Player1 = players[0] ====> x or o
    # Player2 = players[1] ====> x or o

    if first[0] == 'Player 1':
        p = 1
    else:
        p = 2
    
    while full_board_check(board) == False:

        if p == 1:
            display_board(board)
            print('Player 1, place {} on board\n'.format(players[0]))
            marker = players[0]
            board = place_marker(board, marker, player_choice(board))
            p = 2
        
        elif win_check(board, players[0]) == True:
            print('\n'*10 + 'Player 1 wins the game!')
            break

        elif p == 2:
            display_board(board)
            print('Player 2, place {} on board\n'.format(players[1]))
            marker = players[1]
            board = place_marker(board, marker, player_choice(board))
            p = 1
        
        elif win_check(board, players[1]) == True:
            print('\n'*10 + 'Player 2 wins the game!')
            break
         
        if full_board_check(board):
            print('\n'*10 + 'The board is full, no one wins.\n\n\n')

    game_on = replay()

