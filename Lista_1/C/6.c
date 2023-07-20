#include <stdio.h>

int somaDosPares(int A[], int tam, int S) {
    int i, j;
    for (i = 0; i < tam - 1; i++) {
        for (j = i + 1; j < tam; j++) {
            if (A[i] + A[j] == S) {
                return 1; // True
            }
        }
    }
    return 0; // False
}

int main() {
    int A[] = {3, 5, 7, 8, 10};
    int tam = sizeof(A) / sizeof(A[0]);
    int S = 14;

    if (somaDosPares(A, tam, S)) {
        printf("True\n");
    } 
    else {
        printf("False\n");
    }

    return 0;
}

/*
A complexidade será O(n^2), pois existem dois for's alinhados que percorrem o vetor A,
cada um com ordem O(n). Resultando em uma complexidade quadrática.
*/