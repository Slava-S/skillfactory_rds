#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np

def game_core(number):
# Create a function with guess the number

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
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    


# In[ ]:




