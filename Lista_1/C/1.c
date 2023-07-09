#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    int procuraElemento(int array[], int n, int indice, int tamanho){
        if(indice == tamanho){ // caso base
            return -1;
        }
        else if(array[indice] == n){
            return indice;
        }
        return procuraElemento(array, n, indice + 1, tamanho);
    }
    
    
    int array[] = {0,1,2,3,4,5,6};
    int n = 4;
    int tamanho = sizeof(array) / sizeof(array[0]); // calcula o tamanho do vetor
    printf("%d", procuraElemento(array, n, 0, tamanho));
    return 0;
}

