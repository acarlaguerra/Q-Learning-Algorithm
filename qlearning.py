import numpy as np

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
                         [  0  ,  0  ,  0  ,  0  , 0.9 , 0.1 ],
                         [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# RIGHT ------------------------------------------------------ #

# States:                    1     2     3     4     5     6  
matrix_right = np.matrix([[ 0.1 , 0.8 , 0.1 ,  0  ,  0  ,  0  ],
                          [  0  , 0.9 ,  0  , 0.1 ,  0  ,  0  ],
                          [ 0.1 ,  0  ,  0  , 0.8 , 0.1 ,  0  ],
                          [  0  , 0.1 ,  0  , 0.8 ,  0  , 0.1 ],
                          [  0  ,  0  , 0.1 ,  0  , 0.1 , 0.8 ],
                          [  0  ,  0  ,  0  ,  0  ,  0  ,  0  ]])


# --------------------- #
#  Vetor de recompensa  #
# --------------------- #

