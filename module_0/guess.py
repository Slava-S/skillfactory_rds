#!/usr/bin/env python
# coding: utf-8

"""Game guess the number
The computer itself guesses and guesses the number itself
"""

import numpy as np

# Create a function with guess the number
def game_core(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of attempеts
    """
    up = 100                   # up border 
    down = 0                   # down border
    permit = (up + down) / 2   # supposing number is
    count = 1                  # count of attempt
    
    #guessing the number
    while number != permit:
        count = count + 1
        if  number > permit:
            down = permit   
        elif number < permit:
            up = permit    
        permit = round((up + down) / 2)
    return(count)               
    # exit from cicle if guessed 
    
def score_game(game_core):
    '''
    Run the game 1000 times to find out how quickly the game guesses the number
    
    Args:
        random_predict ([type]): fuя

    Returns:
        int: среднее количество попыток
    '''
    count_ls = []
    np.random.seed(1)  # fix RANDOM SEED so that your experiment is reproducible!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Algorithm guesses the number on average for {score} attempt")
    return(score)
    
if __name__ == "__main__":
    # RUN
    score_game(random_predict)

# In[ ]:




