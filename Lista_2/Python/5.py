def menorDiff(A, B, k):

    i_res = None  # Variável para armazenar o valor de i
    j_res = None  # Variável para armazenar o valor de j
    diff_min = float('inf')  # Inicializa a menor diferença como infinito / -infinity

    for a in A:
        # Para cada elemento a em A, encontre o elemento b em B mais próximo de k - a
        target_diff = k - a
        mproxB = min(B, key=lambda x: abs(target_diff - x))

        # Calcula a diferença absoluta entre o valor de k e a soma a + b
        diffAtual = abs(target_diff - mproxB)

        # Atualiza os valores de i_res e j_res se a diferença atual for menor que a menor diferença encontrada até o momento
        if diffAtual < diff_min:
            diff_min = diffAtual
            i_res = a
            j_res = mproxB

    return i_res, j_res

A = [1,5,4,6,8,7,9]
B = [15,46,79,481,1,5,54,6]
k = 481 # target ou alvo

print(menorDiff(A,B,k))