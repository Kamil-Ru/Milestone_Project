def user_choice():
    
    # Variables
    
    #Initial
    choice = 'WRONG'
    acceptable_range = range(1,10)
    withing_range = False
    
    # TWO CONDITION TO CHECK
    #DIGIT OR WITHIN_RANGE == False
    
    while choice.isdigit() == False or withing_range == False:
        
        choice = input("Please enter number (0-10): ")
        
        # DIGIT CHECK
        if choice.isdigit() == False:
             print("Sorry that is not digit!")
                
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                withing_range = True
            else:
                print('Sorry, you are out of acceptable range 0-10')
                withing_range = False
            

    return int(choice)

    
