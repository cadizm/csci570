
/*
    C implementation of Mergesort algorithm
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int* mergesort(int* L, int len)
{
    if (len == 0) {
        return 0;
    }

    if (len == 1) {
        int* res = malloc(sizeof(int));
        *res = *L;

        return res;
    }

    if (len == 2) {
        int* res = calloc(2, sizeof(int));
        res[0] = L[0];
        res[1] = L[1];

        if (res[0] > res[1]) {
            int temp = res[0];
            res[0] = res[1];
            res[1] = temp;
        }

        return res;
    }

    else {
        int i, j, k;
        int mid = len >> 1;
        int T1[mid];
        for (i = 0; i < mid; ++i) {
            T1[i] = L[i];
        }
        int* L1 = mergesort(T1, mid);

        i = 0;
        int rest = len - mid;
        int T2[rest];
        for (j = mid; j < len; ++j) {
            T2[i++] = L[j];
        }
        int* L2 = mergesort(T2, rest);

        int* L3 = calloc(len, sizeof(int));
        i = j = k = 0; /* reset */

        while (1) {
            if (i == mid) {
                while (j < rest)
                    L3[k++] = L2[j++];
                break;
            }
            if (j == rest) {
                while (i < mid)
                    L3[k++] = L1[i++];
                break;
            }
            if (L1[i] < L2[j]) {
                L3[k++] = L1[i++];
            }
            else {
                L3[k++] = L2[j++];
            }
        }

        if (len > 2) {
            free(L1);
            free(L2);
        }

        return L3;
    }
}

int main()
{
    int len = 5;
    int input[] = { 2, 1, 3, 4, -2 };

    printf("Input:  [");
    for (int i = 0; i < len-1; ++i) {
        printf("%d, ", input[i]);
    }
    printf("%d]\n", input[len-1]);

    int* res = mergesort(input, len);

    printf("Result: [");
    for (int i = 0; i < len-1; ++i) {
        printf("%d, ", res[i]);
    }
    printf("%d]\n", res[len-1]);

    free(res);

    return 0;
}
