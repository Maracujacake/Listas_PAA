#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // função que verifica palíndromos (iterativa) em C (quase identica à versão em python)
    int verificaPalindromo(char palavra[]){
        int tamanho = strlen(palavra);
        for(int i = 0; i < tamanho / 2; i++){
            if(palavra[i] != palavra[tamanho - 1 - i]){
                return -1;
            }
        }
        return 1;
    }
    
    // falso teste
    char palavra[] = "arkara";
    printf("%d\n", verificaPalindromo(palavra));


    // versão recursiva que identifica se é palindromo
    int verificaPalindromoRec(char palavra[]){
        int tamanho = strlen(palavra);
        
        int verificaPRAux(int inicio, int fim){
            if(inicio >= fim){
                return 1;
            }
            
            if(palavra[inicio] != palavra[fim]){
                return -1;
            }
            
            verificaPRAux(inicio + 1, fim - 1);
        }
        
        verificaPRAux(0, tamanho - 1);
    }

    char palavra2[] = "elele";
    printf("%d", verificaPalindromoRec(palavra2));
    return 0;
}
