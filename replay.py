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

# print(replay())
