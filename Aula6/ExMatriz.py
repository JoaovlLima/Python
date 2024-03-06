import numpy as np

empty_array = np.empty((3, 3)) # Para criar uma matriz NumPy vazia
print(empty_array)


ones_array = np.ones((2, 2)) #Para criar uma matriz preenchida com valores iguais a 1                    
print(ones_array)


zeros_array = np.zeros((4, 4)) # Para criar uma matriz preenchida com todos os zeros
print(zeros_array)


random_array = np.random.rand(3, 3) #valores Randons
print(random_array)


my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #Para selecionar elementos específicos de uma matriz NumPy
print(my_array)
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

# Valor maximo e minimo 
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")


total_sum = np.sum(my_array) #Para calcular a soma dos valores em uma matriz
print(f"Soma total: {total_sum}")


squeezed_array = np.squeeze(my_array) #Para remover entradas unidimensionais de uma matriz
print(squeezed_array)


#Adição de Matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)


#Subtração de Matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)


#Multiplicação de Matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

#media, mediana e desvio padrao
 
media = np.mean(matriz1)
mediana = np.median(matriz1)
dp = np.std(matriz1)
print("Media, mediana e desvio padrão:")
print(media, mediana, dp)

#soma diagonais 
matriz_quadrada = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Função para calcular a soma das diagonais principal e secundária
def soma_diagonais(matriz):
    diagonal_principal = np.trace(matriz)
    diagonal_secundaria = np.trace(np.flipud(matriz))

    return diagonal_principal, diagonal_secundaria

# Calcular a soma das diagonais
soma_diagonal_principal, soma_diagonal_secundaria = soma_diagonais(matriz_quadrada)

# Imprimir resultados
print("Matriz Quadrada:")
print(matriz_quadrada)

print("\nSoma da Diagonal Principal:", soma_diagonal_principal)
print("Soma da Diagonal Secundária:", soma_diagonal_secundaria)


#num de linhas

numLinha = matriz_quadrada.shape[0]
print("num de Linhas")
print(numLinha)

