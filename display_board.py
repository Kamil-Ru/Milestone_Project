# Write a function that can print out a board. 
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.
# print('\n'*100)
def display_board(board):
    return print('\n'*5 + """
    -------------\t\t\t-------------
    | {} | {} | {} |\t\t\t| 7 | 8 | 9 |
    -------------\t\t\t-------------
    | {} | {} | {} |\t\t\t| 4 | 5 | 6 |
    ------------- \t\t\t-------------
    | {} | {} | {} |\t\t\t| 1 | 2 | 3 |
    -------------\t\t\t-------------""".format(board[7],board[8],board[9],board[4],board[5], board[6], board[1], board[2], board[3]))
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)