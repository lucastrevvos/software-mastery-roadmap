#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char *text = argv[1];
    int letters = 0;

    if (argc != 2)
    {
        printf("usage: ./broken text\n");
        return 1;
    }

    for (int i = 0; i <= strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }

    printf("letters: %i\n", letters);
    return 0;
}
