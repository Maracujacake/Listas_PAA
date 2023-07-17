#versão iterativa para verificar palindromos

palavra = "arara"
def verificaPalindromo(palavra):
    # considera que todas as letras são maiusculas ou minusculas
    # caso sejam diferentes, usar: palavra = palavra.lower();
    tamanho = len(palavra)
    i = 0
    for i in range(tamanho // 2): # percorre somente a metade, pois a outra metade deve ser igual
        if palavra[i] != palavra[tamanho - 1 - i]:
            return False
    return True

verificacao = verificaPalindromo(palavra)
print(verificacao)

#versao recursiva para identificar palindromos
def verificaPalindromoRec(palavra, indice = 0):
    if len(palavra) <= 1:
        return True
    elif palavra[0] != palavra[-1]:  # em python, uso de indices negativos se refere ao final da string para o começo
        return False
    else:
        return verificaPalindromoRec(palavra[1:-1])  #recursivamente passa a fatia entre o primeiro e o ultimo

verificacao2 = verificaPalindromoRec(palavra)
print(verificacao2)


def verificaPalindromoUL(palavra):
    return palavra == palavra[::-1] # percorre a string, de trás para frente, comparando os caracteres

verificacao3 = verificaPalindromoUL(palavra)
print(verificacao3)