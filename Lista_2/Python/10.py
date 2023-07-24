def floor(x):
    return int(x // 1)

def vetor_belo(A, s):
    if not A:
        return False

    # Verifica se a soma dos elementos do vetor é igual a s.
    if sum(A) == s:
        return True

    n = len(A)
    meio = floor((max(A) + min(A)) / 2)

    # Divide o vetor A em duas metades
    esquerda = [x for x in A if x <= meio]
    direita = [x for x in A if x > meio]

    # Chama a função recursivamente para uma das metades
    return vetor_belo(esquerda, s) or vetor_belo(direita, s)