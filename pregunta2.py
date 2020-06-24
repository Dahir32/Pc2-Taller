import random
def  crea_arreglo():

    filas=int(input("Ingrese el primer valor:"))
    columnas=int(input("Ingrese el segundo valor:"))
    matriz=[]
    for w in range(filas):
        matriz.append([0]*columnas)

    for n in range(0,5):
        for i in range(0,filas):
            for j in range(0,columnas):
                numero=random.randrange(0,9)
                matriz[i][j]=numero
        
    print (matriz)

crea_arreglo() 
