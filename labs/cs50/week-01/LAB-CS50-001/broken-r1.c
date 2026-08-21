#include <stdio.h>

int main(void)
{
    double total = 7;
    int people = 2;
    float average = total / people;

    int score = 9;

    if (score == 10)
    {
        printf("perfect\n");
    }

    for (int i = 1; i <= 3; i++)
    {
        printf("%i\n", i);
    }

    printf("average: %.1f\n", average);

    return 0;
}
