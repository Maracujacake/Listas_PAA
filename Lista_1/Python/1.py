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

# Complexidade O(n), visto que percorre o vetor por inteiro uma vez buscando o elemento