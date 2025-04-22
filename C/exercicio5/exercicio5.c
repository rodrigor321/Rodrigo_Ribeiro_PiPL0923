#include <stdio.h>
#include <stdbool.h>

void sort(int nums[3]) {
    for(int k = 0; k < 3; k++) {
        for(int i = 0; i < 3; i++) {
            if(nums[i] > nums[k]) {
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
            }
        }
    }
}

int main() {
    int nums[3] = {0};
    printf("escreva o primeiro numero: ");
    scanf("%i", &nums[0]);
    printf("escreva o segundo numero: ");
    scanf("%i", &nums[1]);
    printf("escreva o terceiro numero: ");
    scanf("%i", &nums[2]);

    sort(nums);

    printf("Crescente: {");
    for(int i = 0; i < 3; i++) {
        printf("%i", nums[i]);
        if(i < 2) {
            printf(",");
        } else {
            printf("}\n");
        }
    }

    printf("Decrescente: {");
    for(int i = 2; i >= 0; i--) {
        printf("%i", nums[i]);
        if(i > 0) {
            printf(",");
        } else {
            printf("}\n");
        }
    }
}
