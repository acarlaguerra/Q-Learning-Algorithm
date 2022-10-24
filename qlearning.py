import numpy as np
import random

# --------------------- #
# Matrizes de transição #
# --------------------- #

# UP --------------------------------------------------------- #

# States:                 1     2     3     4     5     6  
matrix_up = np.matrix([[ 0.1 , 0.1 , 0.8 ,  0  ,  0  ,  0  ],
                       [ 0.1 , 0.1 ,  0  , 0.8 ,  0  ,  0  ],
                       [  0  ,  0  , 0.1 , 0.1 , 0.8 ,  0  ],
                       [  0  ,  0  , 0.1 , 0.1 ,  0  , 0.8 ],
                       [  0  ,  0  ,  0  ,  0  , 0.9 , 0.1 ],
                       [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# DOWN ------------------------------------------------------- #

# States:                   1     2     3     4     5     6  
matrix_down = np.matrix([[ 0.9 , 0.1 ,  0  ,  0  ,  0  ,  0  ],
                         [ 0.1 , 0.9 ,  0  ,  0  ,  0  ,  0  ],
                         [ 0.8 ,  0  , 0.1 , 0.1 ,  0  ,  0  ],
                         [  0  , 0.8 , 0.1 , 0.1 ,  0  ,  0  ],
                         [  0  ,  0  , 0.8 ,  0  , 0.1 , 0.1 ],
                         [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# LEFT ------------------------------------------------------- #

# States:                   1     2     3     4     5     6  
matrix_left = np.matrix([[ 0.9 ,  0  , 0.1 ,  0  ,  0  ,  0  ],
                         [ 0.8 , 0.1 ,  0  , 0.1 ,  0  ,  0  ],
                         [ 0.1 ,  0  , 0.8 ,  0  , 0.1 ,  0  ],
                         [  0  , 0.1 , 0.8 ,  0  ,  0  , 0.1 ],
                         [  0  ,  0  ,  0.1  ,  0  , 0.9 , 0 ],
                         [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# RIGHT ------------------------------------------------------ #

# States:                    1     2     3     4     5     6  
matrix_right = np.matrix([[ 0.1 , 0.8 , 0.1 ,  0  ,  0  ,  0  ],
                          [  0  , 0.9 ,  0  , 0.1 ,  0  ,  0  ],
                          [ 0.1 ,  0  ,  0  , 0.8 , 0.1 ,  0  ],
                          [  0  , 0.1 ,  0  , 0.8 ,  0  , 0.1 ],
                          [  0  ,  0  , 0.1 ,  0  , 0.1 , 0.8 ],
                          [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# ---------------------- #
#  Matriz de recompensa  #
# ---------------------- #

#UP DOWN LEFT RIGHT
## DECIDIR TAMANHO DA MATRIZ DE RECOMPENSAS
reward_matrix = np.full((6,4), -1)

# posição 1 recebe -10 em tentativas de ações DOWN E LEFT
reward_matrix[0,1] = -10
reward_matrix[0,2] = -10

# posição 2 recebe -10 em tentativas de ações DOWN E RIGHT
reward_matrix[1,1] = -10
reward_matrix[1,3] = -10

# posição 3 recebe -10 em tentativas de ações LEFT
reward_matrix[2,2] = -10

# posição 4 recebe -10 em tentativas de ações RIGHT, + 10 para UP
reward_matrix[3,3] = -10
reward_matrix[3,0] = 10

# posição 5 recebe -10 em tentativas de ações UP E LEFT, +10 para RIGHT
reward_matrix[4,0] = -10
reward_matrix[4,2] = -10
reward_matrix[4,3] = 10


# --------------------- #
#        MATRIZ Q       #
#        E AFINS        #
# --------------------- #

Q_matrix = np.zeros(6,4)
Q_matrix[5,0] = 10
Q_matrix[5,1] = 10
Q_matrix[5,2] = 10
Q_matrix[5,3] = 10

alpha = 0.5
gamma = 1

actions_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# ---------------------- #
#        FUNÇÕES         #
# ---------------------- #
#função de inicialização, cálculo do resultado de ações e de atualização de Q

#função de atualização de Q
def Q_update(curr_state, action_index, next_state):
    possible_q = reward_matrix[curr_state] + gamma * max(Q_matrix[next_state])
    value_q = Q_matrix[curr_state, action_index] + alpha(possible_q - Q_matrix[curr_state, action_index])
    return value_q


#função de inicialização
for i in range(25):
    curr_state = 0
    the_end = False

    while not the_end:
        num_rand = random.randint(0,3)

        if(num_rand == 0):
            transition_state = matrix_up[curr_state]
        elif(num_rand == 1):
            transition_state = matrix_down[curr_state]
        elif(num_rand == 2):
            transition_state = matrix_left[curr_state]
        else:
            transition_state = matrix_right[curr_state]

        ##chama a função pra calcular o próximo estado next_state = 

        Q_matrix[curr_state, num_rand] = Q_update(curr_state, num_rand, next_state)

        curr_state = next_state

        if (curr_state == 6):
            the_end = True
