def functionComplexity(n):
    for i in range(n):
        print("esta é a fn1")
        for j in range(n):
            print("esta é a fn2")
            for k in range(n):
                print("esta é a fn3")

#Supondo que fn1 tem complexidade de tempo O(1) e irá executar n vezes, dizemos que a complexidade
#desta parte do loop é O(n).

#Agora, supondo que a complexidade tempo de fn2 é O(n) e esta irá executar n vezes, dizemos que a
#complexidade desta parte do loop é O(n^2).

#Por fim, como fn3 tem O(n^2) e também irá executar n vezes, a complexidade desta parte do código
#é O(n^3), e por ser a maior e a que predomina, também é a resposta da questão.

#Resposta: A complexidade do algoritmo é O(n^3).