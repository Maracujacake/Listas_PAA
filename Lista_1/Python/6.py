array = [1, 3, 4]
s = 6

def somaDois(array, s):
    for i in range(len(array)):
        complemento = s - array[i]
        for k in range(i + 1, len(array)):
            if array[k] == complemento:
                return True
    return False

print(somaDois(array, s))

# A complexidade do algoritmo é O(n^2), pois procura o complementar de cada elemento do array pelo array inteiro
# Uma forma de diminuir a complexidade de tempo para linear O(n) seria a utilização de uma hashset