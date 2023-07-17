#include <stdio.h>

int main()
{
    for(int i = 0; i < n; i++){
        printf("Função fn1()");
        for(int j = 0; j < n; j++){
            printf("Função fn2()");
            for(int k = 0; k < n; k++){
                printf("Função fn3()");
            }
        }
    }
    
/*
Ao saber que a função fn1() possui complexidade O(1) e vai executar n vezes, a complexidade daquela parte do código se torna O(n)
Já a função fn2(), que possui complexiddade O(n), também vai executar n vezes, tornando a complexidade daquela parte O(n^2)
Por fim, a função fn3(), que possui O(n^2), também executando n vezes, vai levar aquela parte do código à possuir O(n^3) e
por ser a complexidade mais relevante, esta é a resposta do exercício. A complexidade de tempo do algoritmo é O(n^3).
*/

    return 0;
}
