"""

a) 

Para encontrar a quantidade de vezes que a função VERIFICAR é aplicada em uma matriz 4x4,
teriamos que contar quantas vezes cada elemento chamaria essa função.

Dependendo do posicionamento do elemento, ele chamara mais ou menos vezes. Logo, vamos
separar por etapas, de acordo com o posicionamento:

Elementos centrais: em uma matriz 4x4, temos 4 elementos centrais. Cada elemento chamará
a função VERIFICAR 4 vezes. Aplicando isso para todos eles, teremos 16 chamadas.

Elementos das laterais(com exceção dos cantos): nessa matriz teremos 8 elementos laterais.
Cada elemento chamará a função 3 vezes. Logo, teremos 24 chamadas.

Elementos dos cantos: temos 4 elementos nos cantos. Cada um deles chamará a função 2 vezes.
Assim, teremos 8 chamadas.

Portanto, somando tudo, totaliza 48 chamadas da função VERIFICAR.

b)

Dividindo a matriz 4x4 em quatro matrizes 2x2, teriamos apenas elementos "dos cantos", aqueles
que realizam apenas 2 chamadas da função VERIFICAR, cada matriz possui 4 elementos. Multiplicando, 
cada matriz chamaria a função 8 vezes. Como temos quatro matrizes, seria necessário chamar a função
32 vezes. Sendo um número menor do que o encontrado anteriormente. Isso acontece porque dividimos 
o nosso problema em problemas menores, o que diminui a quantidade de chamadas recursivas.

c) Foi utilizada a Divisão e Conquista.

"""

#d) 

def VERIFICAR(x, y):
    return x <= y

def minimo_local(matriz, lin_ini, col_ini, lin_fim, col_fim):
    if lin_ini > lin_fim or col_ini > col_fim:
        return False

    lin_med = (lin_ini + lin_fim) // 2
    col_med = (col_ini + col_fim) // 2

    valor_min = matriz[lin_med][col_med]

    # Verificar os vizinhos, menos a diagonal
    if lin_med > 0 and VERIFICAR(matriz[lin_med][col_med], matriz[lin_med - 1][col_med]):
        return False
    if lin_med < len(matriz) - 1 and VERIFICAR(matriz[lin_med][col_med], matriz[lin_med + 1][col_med]):
        return False
    if col_med > 0 and VERIFICAR(matriz[lin_med][col_med], matriz[lin_med][col_med - 1]):
        return False
    if col_med < len(matriz[0]) - 1 and VERIFICAR(matriz[lin_med][col_med], matriz[lin_med][col_med + 1]):
        return False

    # Verificar recursivamente nas sub-matrizes
    if (lin_med > lin_ini and minimo_local(matriz, lin_ini, col_ini, lin_med - 1, col_fim)):
        return True

    if (lin_med < lin_fim and minimo_local(matriz, lin_med + 1, col_ini, lin_fim, col_fim)):
        return True

    if (col_med > col_ini and minimo_local(matriz, lin_ini, col_ini, lin_fim, col_med - 1)):
        return True

    if (col_med < col_fim and minimo_local(matriz, lin_ini, col_med + 1, lin_fim, col_fim)):
        return True

    return False