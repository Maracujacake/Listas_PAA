def ehPrimo(n, divisor = 2):
    if n <= 1:
        return False
    if n <= divisor:
        return True
    if n % divisor == 0:
        return False
    return ehPrimo(n, divisor + 1)

numero = 19
print(ehPrimo(numero))

# Complexidade de tempo O(n)
# Visto que o algoritmo irá continuar executando até o valor se tornar igual ao número passado ou então 1 unidade menor