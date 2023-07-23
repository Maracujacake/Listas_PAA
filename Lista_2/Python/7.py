# a) o mergeSort gera 2^h subproblemas onde h é a altura da árvore de recursão, isto é, a cada
# chamada recursiva, dois novos subproblemas são gerados, cada um com metade do tamanho do problema anterior

# b) o tamanho de cada um destes subproblemas é a metade do problema anterior, logo, n/2, onde n é
# o tamanho do vetor original

# c) somente no passo de ordenação, sem contar as recursões, são realizados O(n) passos, onde
# dois subvetores são mesclados para gerar um único vetor ordenado.

# d) a recorrência do mergeSort é dada por 2T * (n/2) + O(n), onde 2T representa que ocorrem
# duas chamadas recursivas (para dividir o vetor em dois subproblemas), n/2 representa que cada
# subproblema possui metade do tamanho do problema original e O(n) representa o tempo para realizar
# as operações de ordenação em cada um dos subvetores gerados anteriormente.

# e) o último nível h da árvore de recursão é dado por log_2 n, pois o vetor original é dividido em 2 subproblemas
# até que possua apenas um único elemento, não sendo assim capaz de se dividir novamente e estando automaticamente ordenado
# (afinal só há um único elemento).