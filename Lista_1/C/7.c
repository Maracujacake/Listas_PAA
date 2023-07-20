#include <stdio.h>

typedef struct {
    int x, y;
} Coord;

typedef struct {
    Coord infEsq;  // coordenada do canto inferior esquerdo
    Coord supDir;    // coordenada do canto superior direito
} Retangulo;

int retSobrepostos(Retangulo ret1, Retangulo ret2) {
    // não sobreposição no eixo x
    if (ret1.supDir.x < ret2.infEsq.x || ret2.supDir.x < ret1.infEsq.x)
        return 0;

    // não sobreposição no eixo y
    if (ret1.supDir.y < ret2.infEsq.y || ret2.supDir.y < ret1.infEsq.y)
        return 0;

    return 1;
}

/*
A coplexidade será constante O(1), pois só foi necessário fazer duas comparações. 
*/