import numpy as np
import random

# --------------------- #
# Matrizes de transição #
# --------------------- #

# UP --------------------------------------------------------- #

# States:                1     2     3     4     5     6  
matrix_up = np.array([[ 0.1 , 0.1 , 0.8 ,  0  ,  0  ,  0  ],
                      [ 0.1 , 0.1 ,  0  , 0.8 ,  0  ,  0  ],
                      [  0  ,  0  , 0.1 , 0.1 , 0.8 ,  0  ],
                      [  0  ,  0  , 0.1 , 0.1 ,  0  , 0.8 ],
                      [  0  ,  0  ,  0  ,  0  , 0.9 , 0.1 ],
                      [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# DOWN ------------------------------------------------------- #

# States:                  1     2     3     4     5     6  
matrix_down = np.array([[ 0.9 , 0.1 ,  0  ,  0  ,  0  ,  0  ],
                        [ 0.1 , 0.9 ,  0  ,  0  ,  0  ,  0  ],
                        [ 0.8 ,  0  , 0.1 , 0.1 ,  0  ,  0  ],
                        [  0  , 0.8 , 0.1 , 0.1 ,  0  ,  0  ],
                        [  0  ,  0  , 0.8 ,  0  , 0.1 , 0.1 ],
                        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# LEFT ------------------------------------------------------- #

# States:                  1     2     3     4     5     6  
matrix_left = np.array([[ 0.9 ,  0  , 0.1 ,  0  ,  0  ,  0  ],
                        [ 0.8 , 0.1 ,  0  , 0.1 ,  0  ,  0  ],
                        [ 0.1 ,  0  , 0.8 ,  0  , 0.1 ,  0  ],
                        [  0  , 0.1 , 0.8 ,  0  ,  0  , 0.1 ],
                        [  0  ,  0  , 0.1 ,  0  , 0.9 ,  0  ],
                        [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# RIGHT ------------------------------------------------------ #

# States:                   1     2     3     4     5     6  
matrix_right = np.array([[ 0.1 , 0.8 , 0.1 ,  0  ,  0  ,  0  ],
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

Q_matrix = np.zeros((6,4))
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

#função para calcular o próximo estado
def to_next_state(transition_row):
    next_list = []

    #queremos guardar os valores não nulos da linha da matriz
    for index in range(len(transition_row)):

        if transition_row[index] != 0:
            next_list.append((transition_row[index], index))


    #ordenamos a nossa lista a partir do primeiro elemento de cada tupla
    type = [('t_row', float), ('index', int)]
    aux_nlist = np.array(next_list, dtype=type)
    sorted_nlist = np.sort(aux_nlist, order='t_row')
    ##printar a sorted list

    #somatorio dos valores da t_row
    t_row_sorted = [value[0] for value in sorted_nlist]
    cumulative_sum = np.cumsum(t_row_sorted)

    #escolhendo qual valor será usado no next state
    random_num = random.random()

    var = 0
    for k in range(len(cumulative_sum)):
        if cumulative_sum[k] > random_num:
            var = k
            break
    
    return(sorted_nlist[var])


#função de atualização de Q
def Q_update(curr_state, action_index, next_state):

    possible_q = reward_matrix[curr_state][action_index] + gamma * max(Q_matrix[next_state])
    value_q = Q_matrix[curr_state][action_index] + alpha * (possible_q - Q_matrix[curr_state][action_index])

    return value_q

# ---------------------- #
#      INICIALIZAÇÃO     #
# ---------------------- #

for i in range(25):
    curr_state = 0
    the_end = False

    while not the_end:
        random_action = random.randint(0,3)

        if(random_action == 0):
            transition_state = matrix_up[curr_state]
        elif(random_action == 1):
            transition_state = matrix_down[curr_state]
        elif(random_action == 2):
            transition_state = matrix_left[curr_state]
        else:
            transition_state = matrix_right[curr_state]

        next_state = to_next_state(transition_state)

        Q_matrix[curr_state][random_action] = Q_update(curr_state, random_action, next_state[1])

        curr_state = next_state[1]

        if (curr_state == 5):
            the_end = True
