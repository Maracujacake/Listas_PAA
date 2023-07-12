string = "hello world"

def contemDuplicatas(string):
    for i in range(0, len(string)):
        for j in range(1, len(string)):
            if string[i] == string[j]:
                return print('Há caracteres duplicados.')
    print ('Não há caracteres duplicados.')

contemDuplicatas(string)

# Complexidade O(n^2) pois compara cada elemento com o resto do array, percorrendo-o várias vezes