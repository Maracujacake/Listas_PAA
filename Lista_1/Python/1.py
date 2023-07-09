vetor = [0,1,2,3,11,5,6]

def buscaRecursiva(vetor, n, indice = 0):
    if(indice >= len(vetor)): #caso base / restrição
        return False
    elif(n == vetor[indice]): # achou o elemento
        return indice
    else:
        return buscaRecursiva(vetor, n, indice + 1) # chama recursivamente incrementando o índice

# exemplo de uso
resultado = buscaRecursiva(vetor, 11)
print(resultado)

# A complexidade de tempo desta função é O(n), ou seja, proporcional ao tamanho do vetor (pior caso).
# A complexidade de memória é O(1), visto que independe da entrada, somente de variáveis locais.
