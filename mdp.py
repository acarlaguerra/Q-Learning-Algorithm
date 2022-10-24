import numpy as np

#initilizing parameters
gamma = 1

states = np.zeros((3, 2))

rewards = {}
for i in states:
    if i == (3, 1): ## estado final requisitado
        rewards[i] = 1
    elif i == (3, 2): ## estado final evitado
        rewards[i] = -1 
    else:
        rewards[i] = 0 ##inicialização dos demais estados

m_up = np.zeros((6, 6))
#posição 1
m_up[1, 1] = 0.1
m_up[1, 2] = 0.8
m_up[1, 4] = 0.1
#posição 2
m_up[2, 2] = 0.1
m_up[2, 3] = 0.8
m_up[2, 5] = 0.1
#posição 4
m_up[4, 1] = 0.1
m_up[4, 4] = 0.1
m_up[4, 5] = 0.8
#posição 5
m_up[5, 2] = 0.1
m_up[5, 6] = 0.8
m_up[5, 5] = 0.1

m_down = np.zeros((6, 6))
#posição 1
m_down[1, 1] = 0.9
m_down[1, 4] = 0.1
#posição 2
m_down[2, 2] = 0.1
m_down[2, 1] = 0.8
m_down[2, 5] = 0.1
#posição 4
m_down[4, 4] = 0.9
m_down[4, 1] = 0.1
#posição 5
m_down[5, 2] = 0.1
m_down[5, 4] = 0.8
m_down[5, 5] = 0.1


m_right = np.zeros((6, 6))
#posição 1
m_up[1, 1] = 0.1
m_up[1, 2] = 0.1
m_up[1, 4] = 0.8
#posição 2
m_up[2, 1] = 0.1
m_up[2, 3] = 0.1
m_up[2, 5] = 0.8
#posição 4
m_up[4, 4] = 0.9
m_up[4, 5] = 0.1
#posição 5
m_up[5, 4] = 0.1
m_up[5, 6] = 0.1
m_up[5, 5] = 0.8

m_left = np.zeros((6, 6))
#posição 1
m_up[1, 1] = 0.9
m_up[1, 2] = 0.1
#posição 2
m_up[2, 1] = 0.1
m_up[2, 2] = 0.8
m_up[2, 3] = 0.1
#posição 4
m_up[4, 1] = 0.8
m_up[4, 4] = 0.1
m_up[4, 5] = 0.1
#posição 5
m_up[5, 2] = 0.8
m_up[5, 4] = 0.1
m_up[5, 6] = 0.1



