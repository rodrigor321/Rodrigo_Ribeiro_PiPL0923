#include <stdio.h>

int sum(int* arr, int length) {
    int total = 0;
    for (int i = 0; i < length; i++) {
        total += arr[i];
    }
    return total;
}

int clamp(int min, int max, int n) {
    if (n < min) return min;
    if (n > max) return max;
    return n;
}

int main() {
    int notas[10], acima_media = 0;
    
    for (int i = 0; i < 10; i++) {
        printf("Introduza a nota do aluno %i: ", i + 1);
        scanf("%i", &notas[i]);
        notas[i] = clamp(0, 20, notas[i]);
    }

    int media = sum(notas, 10) / 10;

    for (int i = 0; i < 10; i++) {
        if (notas[i] > media) acima_media++;
    }

    printf("A média foi %i e houve %i alunos acima da média\n", media, acima_media);

    return 0;
}
