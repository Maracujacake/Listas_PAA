# Recorrência encontrada anteriormente: 2T * (n/2) + O(n)

# ao expandir a recorrência anteriormente encontrada algumas vezes, teremos:

#T(n) = 2 * (2T(n/4) + O(n/2)) + O(n)
#= 4T(n/4) + 2 * O(n)
#= 4 * (2T(n/8) + O(n/4)) + 2 * O(n)
#= 8T(n/8) + 3 * O(n)
#= ..... T(n) = 2^k * T(n/2^k) + k * O(n), como podemos ver nos exemplos acima

# substituimos o valor de k para quando n/2^k = 1, ou seja, tenha chegado no caso base e não possa mais ser dividido
# sabemos que a altura da árvore de recursão é log_2(n), logo, substituiremos k por este valor

# T(n) = 2^(log_2(n)) * T(1) + log_2(n) * O(n) -> T(1) representa que no caso base o tempo para ordenar o vetor seria O(1), visto que_
# _ele já está ordenado por haver somente um elemento nele!

# como T(1) é um valor constante, podemos substituí-lo por : T(n) = c * 2^(log_2(n)) + O(n * log_2(n))

#T(n) = c * 2^(log_2(n)) + O(n * log_2(n))
# como 2^(log_2(n)) é = n, podemos substituir:
# T(n) = c * n + O(n * log_2(n))
# definindo-a utilizando a notação big-O, chegamos ao resultado de: O(n * log_2(n))





