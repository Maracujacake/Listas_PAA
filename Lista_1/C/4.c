#include <stdio.h>
#include <stdlib.h>


int main()
{
    char string[] = "Banana";
    int tamString = strlen(string);
    
    
    void haDuplicatas(char *string){
        for(int i = 0; i < tamString; i++){
            for(int j = i + 1; j < tamString; j++){
                if(string[i] == string[j]){
                    return printf("Há caracteres duplicados.");
                }
            }
        } return printf("Não há caracteres duplicados.");
    }
    
    haDuplicatas(string);
    
    return 0;
}
