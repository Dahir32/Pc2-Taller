import numpy as np

a = np.array([[34, 43, 73, 25, 10],
            [ 82,  22,  12,  14, 10],
            [ 53,  94,  66,  84, 10],
            [ 35,  73,  24,  34, 10]])


your_permutation = [4,1,2,3,0]

perm_mat = np.zeros((len(your_permutation), len(your_permutation)))

for idx, i in enumerate(your_permutation):
    perm_mat[idx, i] = 1

print (np.dot(a, perm_mat))