def display_board(board):
    a = print("""
    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    ------------- 
    | {} | {} | {} |
    -------------""".format(board[7],board[8],board[9],board[4],board[5], board[6], board[1], board[2], board[3]))
    return a
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)