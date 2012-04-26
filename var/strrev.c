
#include <stdio.h>
#include <string.h>

void swap(int i, int j, char* str)
{
    char c = str[i];
    str[i] = str[j];
    str[j] = c;
}

void strrev(char* str)
{
    int i = 0;
    int j = strlen(str)-1;
    while(i != j && i < j) {
        swap(i, j, str);
        i++;
        j--;
    }
}

int main()
{
//    char* str = malloc(4*sizeof(char));
//    strcpy(str, "abc");
    char str[100] = "ab\0";
    printf("%s\n", str);
    strrev(str);
    printf("%s\n", str);
}
