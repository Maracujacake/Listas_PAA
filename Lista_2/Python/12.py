# O teste de mesa que será realizado no algoritmo mergeSort tem 3 passos essenciais
# divisão = dividir os vetores na metade até que possuam apenas um elemento, ou seja, já estarão ordenados
# conquista = comparando os vetores, um a um, ordenando-os utilizando dois ponteiros, onde um
#   aponta para o primeiro elemento de um vetor e outro para o primeiro elemento do outro vetor que está sendo analisado
#   sejam estes i e j, caso o elemento apontado por i seja menor que o apontado por j, o elemento de i é adicionado ao
#   vetor resultante e i passa a apontar para o proximo elemento de seu vetor.

# caso exemplo:  A = [8, 4, 3, 17, 25, 5, 12, 10]

# passo 1: dividir
# A1 = [8, 4, 3, 17]
# A2 = [25, 5, 12, 10]

# possuem apenas um elemento? F

#A11 = [8, 4]
#A12 = [3, 17]
#A21 = [25, 5]
#A22 = [12, 10]

# possuem apenas um elemento? F

#A111 = [8]
#A112 = [4]
#A121 = [3]
#A122 = [17]
#A211 = [25]
#A212 = [5]
#A221 = [12]
#A222 = [10]

# possuem apenas um elemento? V
# mesclar e ordenar pares de vetores

#A111 e A112 se tornam [4, 8]
#A121 e A122 se tornam [3, 17]
#A212 e A211 se tornam [5, 25]
#A221 e A222 se tornam [10, 12]

# [3, 4, 8, 17]
# [5, 10, 12, 25]

#  [3, 4, 5, 8, 10, 12, 17, 25]

# a complexidade do algoritmo, como já foi calculada em exercicios anteriores, é dada por O(n log(n))
# visto que o Teorema Mestre é aplicado a recorrências do tipo T(n) = a * T(n/b) + f(n)
# a = numero de chamadas recursivas, b = numero de subproblemas gerados, f(n) = tempo para resolução de cada subproblema
# no mergeSort temos T(n) = ( 2T (n / 2) + O(n) )
# sabendo que se (a = b^d) a complexidade resultante é n^d log(n)
# 2 = 2^1, logo a complexidade é O(n^1 * log(n))
# ou O (n log(n))

