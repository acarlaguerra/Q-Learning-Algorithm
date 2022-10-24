import numpy as np
import random


# | 5 | 6 |
# | 3 | 4 |
# | 1 | 2 |


matriz_rg = [[0.1, 0.8, 0.1, 0, 0, 0],
            [0, 0.9, 0, 0.1, 0, 0],
            [0.1, 0, 0, 0.8, 0.1, 0],
            [0, 0.1, 0, 0.8, 0, 0.1],
            [0, 0, 0.1, 0, 0.1, 0.8],
            [0, 0, 0, 0, 0, 0]]

matriz_up = [[0.1, 0.1, 0.8, 0, 0, 0],
            [0.1, 0.1, 0, 0.8, 0, 0],
            [0, 0, 0.1, 0.1, 0.8, 0],
            [0, 0, 0.1, 0.1, 0, 0.8],
            [0, 0, 0, 0, 0.9, 0.1],
            [0, 0, 0, 0, 0, 0]]

matriz_lf = [[0.9, 0, 0.1, 0, 0, 0 ],
            [0.8, 0.1, 0, 0.1, 0, 0],
            [0.1, 0, 0.8, 0, 0.1, 0],
            [0, 0.1, 0.8, 0, 0, 0.1],
            [0, 0.9, 0.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

matriz_down = [[0.9, 0.1, 0, 0, 0, 0],
              [0.1, 0.9, 0, 0, 0, 0],
              [0.8, 0, 0.1, 0.1, 0, 0],
              [0, 0.8, 0.1, 0.1, 0, 0],
              [0, 0, 0.8, 0, 0.1, 0.1],
              [0, 0, 0, 0, 0, 0]]
              
Q_matriz = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[10]*4]

actions_names = ["UP","LF","DW","RG"]

gamma = 1

alpha = 0.5

rewards = [
    #up ,le ,dw ,ri
    [ -1,-10,-10, -1],
    [ -1, -1,-10,-10],
    [ -1,-10, -1, -1],
    [ 10, -1, -1,-10],
    [-10,-10, -1, 10],
    [  0,  0,  0,  0],
]


def action_result(transition):
    index = 0
    states = {}
    transit = []
    values = []
    for i in transition:
        if i != 0:
            states[index] = i
            transit.append(i)
            values.append(index)
        index += 1
    
    for i in range(len(transit)-1):
        for x in range(len(transit)-1):
            if transit[x+1] < transit[x]:
                transit[x], transit[x+1] = transit[x+1], transit[x]
                values[x], values[x+1] = values[x+1], values[x]
            

    
    somatorium = np.cumsum(transit)
    r = random.random()
    index = 0
    for i in somatorium:
        if i > r:
            break
        index += 1
    
    return values[index]

        
    

def update_func(s,a,_s):
    Q_matriz[s][a] = Q_matriz[s][a] + alpha*((rewards[s][a] + (gamma * max(Q_matriz[_s]))) - Q_matriz[s][a])


def call_all():
    state = 0
    while True:
        trial = random.randint(0, 3)
        if trial == 0:
            transition = matriz_up[state]
        
        elif trial == 1:
            transition = matriz_lf[state]

        elif trial == 2:
            transition = matriz_down[state]

        elif trial == 3:
            transition = matriz_rg[state]
   
        next_state = action_result(transition)


        print(f'Present state: {state};')
        print(f'transition: {transition};') 
        print(f'Movement: {actions_names[trial]};')
        print(f'Next state: {next_state}.\n')
                
        update_func(state, trial, next_state)

        state = next_state

        if state == 5:
            break


for _ in range(15):
    call_all()


def find_direction(s):
    dir = np.argmax(Q_matriz[s])
    if(dir==0):
        return('UP')
    if(dir==1):
        return('LF')
    if(dir==2):
        return('DW')
    if(dir==3):
        return('RG')

print(f'\n ========================================= \n')
print(f' ---------------- {find_direction(4)} | OK ----------------')
print(f' ---------------- {find_direction(2)} | {find_direction(3)} ----------------')
print(f' ---------------- {find_direction(0)} | {find_direction(1)} ----------------')
print(f'\n =========================================')