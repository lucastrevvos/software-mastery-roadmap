#include <stdio.h>


int main(void)
{
    long number;
    long temp;
    int qtd_digits = 0;
    int sum_digits = 0;
    int last_digit = 0;

    do
    {
        printf("Digite um numero inteiro positivo: ");
        scanf("%ld", &number);

    } while (number <= 0);

    temp = number;

    //Processa os digitos com matematica (% e /)
    while( temp > 0)
    {
        last_digit = temp % 10; // Ultimo digito
        sum_digits = sum_digits + last_digit; // Pega o ultimo digito e soma
        qtd_digits++;

        temp = temp / 10; // Remove o ultimo digito
    }

    printf("Quantidade de digitos = %i\n", qtd_digits);
    printf("Soma dos digitos = %i", sum_digits);
}
