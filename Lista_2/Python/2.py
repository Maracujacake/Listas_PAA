def multiplicaMatriz(X, Y):
    n = len(X) # pega o tamanho da matriz, como ambas são iguais
    Z = [ [0] * n for _ in range(n) ] # cria a matriz Z de tamanho n com todos os elementos zerados

# percorre com uma mesma linha todas as colunas da outra matriz, fazendo a multiplicação e a adição destas multiplicações
# e então colocando esse valor resultante na posição da matriz Z
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z


# teste
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print(multiplicaMatriz(X, Y))

# a complexidade deste algoritmo, isto é, do algoritmo padrão para a multiplicação de matrizes
# é de O(n^3), visto que visita cada elemento de cada coluna para cada linha (n^3).

# No algoritmo de Strassen é utilizado o princípio de divisão e conquista para chegar a uma solução mais eficiente