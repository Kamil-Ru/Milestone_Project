# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again

    #   OLD:

def replay():
    loop = False
    while loop == False:
        chose = input('Do you want to play again?\nType: "y" - for yes\nType: "n" - for no\n')
        if chose == 'y':
            loop = True
            return True
        elif chose == 'n':
            loop = True
            return False
        else:
            loop = False

# NEW: 

def replay_2():
    while True:
        chose = input('Do you want to play again?\nType: "y" - for yes\nType: "n" - for no\n')
        if chose == 'y':
            return True 
        elif chose == 'n':
            return False

