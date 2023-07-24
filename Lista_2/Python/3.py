
"""

Como o algoritmo divide o problema pela metade na chamada recursiva FastPower(c, floor(b/2)), 
já podemos considerar que ele terá uma complexidade logaritmica. Como o b que foi dividido,
então temos O(log b). Além disso, temos algumas multiplicações que possuem complexidade
constante O(1). Logo, como O(log b) é dominante, essa será a complexidade do algoritmo.

"""