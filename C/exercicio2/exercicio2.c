#include <stdio.h>

int main() {
    int num1 = 0, num2 = 0, num3 = 0;  
    int maior = 0, menor = 0;  

    printf("Escreva o primeiro numero: ");
    scanf("%d", &num1);
    printf("Escreva o segundo numero: ");
    scanf("%d", &num2);
    printf("Escreva o terceiro numero: ");
    scanf("%d", &num3);

  
    maior = num1;  
    if (num2 > maior) {
        maior = num2;
    }
    if (num3 > maior) {
        maior = num3;
    }

   
    menor = num1;  
    if (num2 < menor) {
        menor = num2;
    }
    if (num3 < menor) {
        menor = num3;
    }

    printf("O maior numero é: %d\n", maior);
    printf("O menor numero é: %d\n", menor);

    return 0;
}
