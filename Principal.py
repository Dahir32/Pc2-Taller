import random
import numpy as np
numero=6
filas=20
columnas=20
matriz=[]
for w in range(filas):
    matriz.append([0]*columnas)

for n in range(0,5):
    for i in range(0,filas):
        for j in range(0,columnas):
            numero=random.randrange(0,9)
            matriz[i][j]=numero
        
print (matriz)

while numero>0:
    your_permutation = [19,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0]

    perm_mat = np.zeros((len(your_permutation), len(your_permutation)))

    for idx, i in enumerate(your_permutation):
        perm_mat[idx, i] = 1
    print (np.dot(matriz, perm_mat))
    numero=numero-1
