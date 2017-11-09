>>> import tf
>>> from tf import transformations
>>> from tf import transformations
>>> transformations.identity_matrix()
array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])
>>> B_T_O = transformations.euler_matrix(0.79,0,0.79,'rxyz')
>>> B_T_O
array([[ 0.70384532, -0.71035327, -0.        ,  0.        ],
       [ 0.49997882,  0.49539823, -0.71035327,  0.        ],
       [ 0.50460177,  0.49997882,  0.70384532,  0.        ],
       [ 0.        ,  0.        ,  0.        ,  1.        ]])
>>> B_T_O += transformations.translation_matrix((0, 1, 1))
