#include <stdio.h>

int sum(int* arr, int lenght) {
    int sum = 0;
    for(int i = 0; i < lenght; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int notas[3];
    int pesos[3] = {2,3,5};
    int pesos_sum = sum(pesos, 3);
    printf("escreva a primeira nota: ");
    scanf("%i", &notas[0]);
    printf("escreva a segunda nota: ");
    scanf("%i", &notas[1]);
    printf("escreva a terceira nota: ");
    scanf("%i", &notas[2]);
    int media = 0;
    for(int i = 0; i < 3; i++) {
        media += notas[i] * pesos[i];
    }
    media /= pesos_sum;

    if(media >= 6) {
        printf("APROVADO\n");
    } else {
        printf("REPROVADO\n");
    }
}
