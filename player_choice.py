# Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. 

# If it is, then return the position for later use.

test_board = ['#','X','O','X','O',' ','O','X','O','X']

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def player_choice(board):
    choice = ' '
    acceptable_range = range(1,10)
    withing_range = False

    while choice.isdigit() == False or withing_range == False or space_check(test_board,int(choice)) == False:
        choice = input("Chose one of the free positions on the board (1-9): ")

        if choice.isdigit() == False:
            print("Sorry that is not digit!")
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                withing_range = True
                if space_check(test_board,int(choice)) == False:
                    print("Sorry, position {} is taken".format(choice))
            else:
                print('Sorry, you are out of acceptable choose 1-9')
                withing_range = False      

    return int(choice)

player_choice(test_board)
            
