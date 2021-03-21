# Write a function that takes in the board list object, a marker ('X' or 'O'), 
# and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker
    return board


# place_marker(test_board,'$',8)
# display_board(test_board)