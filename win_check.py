# Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

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
