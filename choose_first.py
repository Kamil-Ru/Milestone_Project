# Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.

import random
#OLD
'''
def choose_first():
    a = random.randint(0, 1)
    if a == 0:
        return list(('Player 1', 'Player 2'))
    elif a == 1: 
        return list(('Player 2', 'Player 1'))
'''
# Test
# print(choose_first())        

# code review
# NEW:
def choose_first_2():
        if random.randint(0, 1) == 1:
            return list(('Player 1', 'Player 2'))
        else:
            return list(('Player 2', 'Player 1'))


print(choose_first_2()) 

'''
test
def choose_first_3(): # draw_first nic nie wybierasz tylko losujesz
    # a = random.randint(0, 1) # Zamiast else if porstu guard będzie lepszy. return list(('Player 1', 'Player 2')) if a == 0 
    # if a == 0:
    #     return list(('Player 1', 'Player 2')) 
    # elif a == 1: 
    #     return list(('Player 2', 'Player 1')
    return list(('Player 1', 'Player 2')) if random.randint(0, 1) == 1
    return list(('Player 2', 'Player 1'))
    
    '''