
#include <stdio.h>
#include <stdlib.h>

struct Set {
    int name;
    int value;
    struct Set* ptr;
};

/*
 * Create an array of Set pointers of length len. Each set
 * has a name and value corresponding to a value of v.
 * Return the array of pointers.
 */
struct Set** MakeSet(int V[], int len)
{
    struct Set** setPtrArr = calloc(len, sizeof(struct Set));
    for (int i = 0; i < len; ++i) {
        struct Set* setPtr = malloc(sizeof(struct Set));
        setPtr->name = V[i];
        setPtr->value = V[i];
        setPtr->ptr = NULL;
        setPtrArr[i] = setPtr;
    }

    return setPtrArr;
}

/*
 * Find the set that contains value v in S
 */
struct Set* FindSet(int v, struct Set** S, int len)
{
    for (int i = 0; i < len; ++i) {
        struct Set* s = S[i];
        if ((int)s->value == v) {
            if (s->name == NULL && s->ptr != NULL) {
                while (s->ptr != NULL) {
                    s = s->ptr;
                }
            }
            // S now has either the first match or the
            // set after its ptr has been followed to
            // the "naming" set
            return s;
        }

    }

    return NULL;
}

/*
 * Union of set's s and t. The name of the set with "smaller"
 * value is used as the name for the new unioned set.
 */
void Union(struct Set* s, struct Set* t)
{
    if (s == t)
        return;

    struct Set* smaller;
    struct Set* bigger;
    if (s->value < t->value) {
        smaller = s;
        bigger = t;
    }
    else {
        smaller = t;
        bigger = s;
    }

    bigger->name = NULL;
    bigger->ptr = smaller;
}


int main()
{
    int len = 4;
    int input[] = { 0, 1, 2, 3 };
    struct Set** sets = MakeSet(input, len);

    Union(sets[0], sets[1]);
    Union(sets[1], sets[2]);
    Union(sets[0], sets[3]);
    Union(sets[0], sets[0]);
    Union(sets[0], sets[3]);
    Union(sets[0], sets[3]);

    int find = 3;
    struct Set* s = FindSet(find, sets, len);
    if (s == NULL) {
        printf("NULL\n");
    }
    else {
        printf("Name of set for value %d: %d\n", find, s->name);
    }

    for (int i = 0; i < len; ++i) {
        free(sets[i]);
    }
    free(sets);

    return 0;
}
