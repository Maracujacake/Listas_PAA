# O teste de mesa que será realizado no algoritmo da soma máxima de subsequência tem 2 passos essenciais
# divisão = dividir os vetores na metade até que possuam apenas um elemento
# conquista = juntar os subvetores para encontrar a maior soma de subsequência


# caso exemplo:  A = [10, 5, -17, 20, 50, -1, 3, -30, 10]

# passo 1: dividir
# A1 = [10, 5, -17, 20]
# A2 = [50, -1, 3, -30, 10]

# possuem apenas um elemento? F

# A11 = [10, 5]
# A12 = [-17, 20]
# A21 = [50, -1]
# A22 = [3, -30, 10]

# possuem apenas um elemento? F

# A111 = [10]
# A112 = [5]
# A121 = [-17]
# A122 = [20]
# A211 = [50]
# A212 = [-1]
# A221 = [3]
# A222 = [-30, 10]

# possuem apenas um elemento? F

# A111 = [10]
# A112 = [5]
# A121 = [-17]
# A122 = [20]
# A211 = [50]
# A212 = [-1]
# A221 = [3]
# A2221 = [-30]
# A2222 = [10]

# possuem apenas um elemento? V
# realizar junção e fazer a soma dos vetores

# A111 e A112 se tornam [10, 5]          
# A121 e A122 se tornam [-17, 20]
# A212 e A211 se tornam [50, -1]
# A221 e A2221 se tornam [3, -30]
# A2222 = [10]

# Opções esquerda:
# 10 + 5 = 15 // -17 + 20 = 3

# Opções Direita:
# 50 + (-1) = 49 // 3 + (-30) = -27 // 10

# continuar junção 

# A111, A112, A121 e A122 se tornam [10, 5, -17, 20]
# A212, A211, A221, A2221 e A2222 se tornam [50, -1, 3, -30, 10]

# Realizar cruzamento das duas metades
# Temos na esquerda [10, 5, -17], soma = -2
# Temos na direita [20, 50, -1, 3], soma = 72 // [10]

# Logo, o vetor da soma máxima de subsequência é [50, -1, 3, -3, 10], com soma = 72.

# A complexidade de cada divisão é O(log n), e a complexidade de cada conquista/junção
# é O(n), resultando em uma complexidade de O(n log n).



