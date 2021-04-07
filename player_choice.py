# Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. 

# If it is, then return the position for later use.

test_board = ['#','X','O','X','O',' ','O','X','O','X']

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

#   NEW:
    
def player_choice_2(board):
    while True:
        try:
            choice = int(input("Chose one of the free positions on the board (1-9): "))
            if choice in range(1,10) and space_check(board,choice):
                return choice
        except:
            print('Sorry, you are out of acceptable choose 1-9')  
            
player_choice_2(test_board)    
    
#   OLD:    

'''
def player_choice(board):
    choice = ' '
    acceptable_range = range(1,10)
    withing_range = False

    while choice.isdigit() == False or withing_range == False or space_check(board,int(choice)) == False:
        choice = input("Chose one of the free positions on the board (1-9): ")

        if choice.isdigit() == False:
            print("Sorry, this is not a digit!")
            
            
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                withing_range = True
                if space_check(board,int(choice)) == False:
                    print("Sorry, position {} is taken".format(choice))
            else:
                print('Sorry, you are out of acceptable choose 1-9')
                withing_range = False      

    return int(choice)

'''

# player_choice(test_board)


            