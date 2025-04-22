#include <stdio.h>

int main() {
    int num1, num2;
    printf("escreva o primeiro numero: ");
    scanf("%d", &num1);
    printf("escreva o segundo numero: ");
    scanf("%d", &num2);

    printf("ordem crescente: ");
    if (num1 < num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }

    printf("ordem decrescente: ");
    if (num1 > num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }

}
