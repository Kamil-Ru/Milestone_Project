# Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.

import random

def choose_first():
    a = random.randint(0, 1)
    if a == 0:
        return str('player1')
    elif a == 1: 
        return str('player2')
