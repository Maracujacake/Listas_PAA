#include <stdio.h>
#include <stdlib.h>


int main()
{
    int array[] = {1, 3, 4, 6, 2, 5, 7, 154};
    
    void selection_sort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        int aux = array[i];
        array[i] = array[min_idx];
        array[min_idx] = aux;
    }
}

    int tam = sizeof(array)/sizeof(array[0]);
    
    selection_sort(array, tam);
    
    for(int k = 0; k < tam; k++){
        printf("%d ", array[k]);
    }

    return 0;
}
