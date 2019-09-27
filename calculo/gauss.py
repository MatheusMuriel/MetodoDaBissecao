import numpy as np
import math

class CalculadoraGauss():

    def __init__(self, A, B):
        # A*X = B
        self.matrizA = A
        self.matrizB = B
        self.matrizX = []
        pass

    def GENP(A, b):
        
        n =  len(A)
        
        for pivot_row in range(n-1):

            for row in range(pivot_row+1, n):
                v1 = A[row][pivot_row]
                v2 = A[pivot_row][pivot_row]

                multiplier = v1 / v2

                #the only one in this column since the rest are zero
                A[row][pivot_row] = multiplier
                for col in range(pivot_row + 1, n):
                    A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
                #Equation solution column
                b[row] = b[row] - multiplier*b[pivot_row]
                A[row][pivot_row] = 0

            ##Aqui vira a iteração 


        # print (A
        # print b
        x = np.zeros(n)
        k = n-1
        x[k] = b[k]/A[k,k]
        while k >= 0:
            x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
            k = k-1
        return x

    #if __name__ == "__main__":
        
        #print(GENP(np.copy(A), np.copy(b)))

def constroi_matriz_A(dictMatriz):
    n = int(math.sqrt( len(dictMatriz) ))
    
    matriz = []
    for linha in range(1, n+1): 
        linha_aux = []
        for coluna in range(1, n):
            nome = str(linha) + str(coluna)
            valor = dictMatriz[nome]
            linha_aux.append(valor)
        matriz.append(linha_aux)

    return np.array(matriz)

def constroi_matriz_B(dictMatriz):
    n = int(math.sqrt( len(dictMatriz) ))
    
    matriz = []
    for linha in range(1, n+1):
        nome = str(linha) + str(n) 
        valor = dictMatriz[nome]
        matriz.append(valor)

    return np.array(matriz)

def factory(dictMatriz):
    aaux = constroi_matriz_A(dictMatriz)
    baux = constroi_matriz_B(dictMatriz)

    A = np.array([  [1.0, 2.0, 3.0, 4.0],
                    [2.0, 1.0, 2.0, 3.0],
                    [3.0, 2.0, 1.0, 2.0],
                    [4.0, 3.0, 2.0, 1.0]])
    b =  np.array([[10.],[7.],[6.],[5.]])

    return CalculadoraGauss(A, b)
