#include <stdio.h>

float get_desconto(float preco) {
    if(preco <= 200) {
        return 0.10;
    } else if(preco > 200 && preco <= 500) {
        return 0.15;
    } else {
        return 0.20;
    }
}

int main() {
    char nome[513] = {0};
    float valor = 0;
    
    printf("Escreva o nome do cliente: ");
    scanf("%[^\n]512s", nome);
    getchar();
    printf("Escreva o valor da compra: ");
    scanf("%f", &valor);
    float desconto = get_desconto(valor);
    printf("Cliente \"%s\", valor da compra: %.2f, valor do desconto: %.2f, valor a pagar: %.2f\n", nome, valor, valor*desconto, valor-(valor*desconto));
    
    return 0;
}
