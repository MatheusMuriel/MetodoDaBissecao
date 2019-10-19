import math

class CalculadoraGauss():

    def __init__(self, A, B, L):
        # A*X = B
        #self.matrizA = np.copy(A)
        self.matrizA = A.copy()
        #self.matrizB = np.copy(B)
        self.matrizB = B.copy()
        self.matrizX = []
        self.passos = []
        self.Passo.contador = 1
        self.matriz_lost = L

    def GENP(self, a, b):

        n =  len(a)
        
        for pivot_row in range(n-1):

            for row in range(pivot_row+1, n):

                v1 = a[row][pivot_row]
                v2 = a[pivot_row][pivot_row]

                
                multiplier = v1 / v2

                if (multiplier == np.Infinity):
                    print("Zeroooo")
                
                self.matriz_lost[row][pivot_row] = multiplier

                #the only one in this column since the rest are zero
                a[row][pivot_row] = multiplier
                for col in range(pivot_row + 1, n):
                    a[row][col] = a[row][col] - multiplier*a[pivot_row][col]
                #Equation solution column
                b[row] = b[row] - multiplier*b[pivot_row]
                a[row][pivot_row] = 0
                passo = self.Passo(a, b)
                self.passos.append(passo)

            ##Aqui vira a iteração 

        x = [0. for _ in range(n)]
        k = n-1
        x[k] = b[k]/a[k,k]
        while k >= 0:
            x[k] = (b[k] - np.dot(a[k,k+1:],x[k+1:]))/a[k,k]
            k = k-1
        return x

    def calcular(self):
        matriz_x = self.GENP(self.matrizA, self.matrizB)
        self.matrizX = matriz_x
        
        list_x = [valor for valor in self.matrizX]
        resposta = {'matriz_x': list_x, 'passos': self.passos}
        return resposta

    """
    TAD para representar um passo da resposta
    """
    class Passo():
        contador = 1
        def __init__(self, A, B):
            self.matrizA = self.convertArrayNumPy(np.copy(A))
            self.matrizB = [valor for valor in B]
            self.numero_passo = self.__class__.contador
            self.__class__.contador += 1
        
        def convertArrayNumPy(self, array_numpy):
                nova_lista = []
                for i in array_numpy:
                    lista_aux = []
                    for j in i:
                        lista_aux.append(j)
                    nova_lista.append(lista_aux)
                return nova_lista
        
        def __str__(self):
            strA = str(self.matrizA)
            strB = str(self.matrizB)
            strNumPasso = str(self.numero_passo)

            strPasso = "$$$" + strNumPasso + "###" + strA + "&&&" + strB
            return strPasso


def constroi_matriz_A(dictMatriz):
    n = int(math.sqrt( len(dictMatriz) ))
    
    matriz = []
    for linha in range(1, n+1): 
        linha_aux = []
        for coluna in range(1, n+1):
            nome = str(linha) + str(coluna)
            valor = dictMatriz[nome]
            linha_aux.append(valor)
        matriz.append(linha_aux)

    return matriz

def constroi_matriz_B(dictMatriz):
    n = int(math.sqrt( len(dictMatriz) ))
    
    matriz = []
    for linha in range(1, n+1):
        nome = str(linha) + str(n+1) 
        valor = dictMatriz[nome]
        matriz.append(valor)

    return matriz

def constroi_matriz_L(tamanho):
    matriz = []
    for i in range(0, tamanho+1):
        linha = []
        for j in range(0, tamanho+1):
            linha.append(1 if j < i+1 else 0)
        matriz.append(linha)
    return matriz

def factory(dictMatriz):
    matriz_a = constroi_matriz_A(dictMatriz)
    matriz_b = constroi_matriz_B(dictMatriz)
    matriz_l = constroi_matriz_L(len(matriz_a))

    return CalculadoraGauss(matriz_a, matriz_b, matriz_l)


Ai = [  [2., -3.,  1.],
        [4., -6., -1.],
        [1.,  2.,  1.]]
bi = [  [-5.],
        [-7.],
        [4.]]

A = [  [1.0, 2.0, 3.0, 4.0],
        [2.0, 1.0, 2.0, 3.0],
        [3.0, 2.0, 1.0, 2.0],
        [4.0, 3.0, 2.0, 1.0]]
b =  [  [10.],
        [7.],
        [6.],
        [5.]]

l = constroi_matriz_L(len(A)-1)

claz = CalculadoraGauss(A, b, l)
claz.calcular()