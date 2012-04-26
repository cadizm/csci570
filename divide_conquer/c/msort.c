/*
    Linked List Mergesort
    Inspired by: A Comparative Study of Linked List Sorting Algorithms
    See: http://www.cs.mtu.edu/~shene/PUBLICATIONS/1996/3Conline.pdf

    TODO: Better pseudo random number generation
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define APPEND(P, H, T) \
Node* next = P->next;\
if (H == NULL) {\
    H = T = P;\
    T->next = NULL;\
}\
else {\
    T->next = P;\
    T = P;\
    T->next = NULL;\
}\
P = next;\

typedef struct Node Node;
struct Node {
    Node* next;
    int data;
};

int compare(Node* e1, Node* e2);
Node* merge(Node* Q, Node* R);
Node* msort(Node* L);
void printL(Node* L);

int compare(Node* e1, Node* e2)
{
    if (!e1 || !e2) {
        return (int)NULL;
    }

    return e1->data - e2->data;
}

Node* merge(Node* Q, Node* R)
{
    if (!Q && !R) {
        return NULL;
    }
    else if (Q && !R) {
        return Q;
    }
    else if (R && !Q) {
        return R;
    }

    /* Both Q and R defined */
    Node* q = Q;
    Node* r = R;

    Node* head = NULL;
    Node* tail = NULL;

    Node* e;
    while (1) {
        if (compare(q, r) < 0) {
            e = q;
            q = q->next;
        }
        else {
            e = r;
            r = r->next;
        }

        if (head == NULL) {
            head = tail = e;
            tail->next = NULL;
        }
        else {
            tail->next = e;
            tail = e;
            tail->next = NULL;
        }

        /* For the next two if's, since we assume the passed lists  */
        /* are sorted, simply append the rest of the remaining list */
        if (q == NULL) {
            tail->next = r;
            break;
        }
        if (r == NULL) {
            tail->next = q;
            break;
        }
    }

    return head;
}

Node* msort(Node* L)
{
    if (L == NULL) {
        return NULL;
    }

    if (L->next == NULL) {
        return L;
    }

    Node* QHead = NULL;
    Node* QTail = NULL;
    Node* RHead = NULL;
    Node* RTail = NULL;

    Node* p = L;
    while (p != NULL) {
        APPEND(p, QHead, QTail);
        if (p != NULL) {
            APPEND(p, RHead, RTail);
        }
    }

    QHead = msort(QHead);
    RHead = msort(RHead);

    return merge(QHead, RHead);
}

void printL(Node* L)
{
    Node* p;

    printf("[");
    for (p = L; p->next != NULL; p = p->next) {
        printf("%d, ", p->data);
    }
    printf("%d]\n", p->data);
}

int main()
{
    int i;
    int N = 7;

    Node* head = NULL;
    Node* tail = NULL;
    int r = time(NULL);
    for (i = 0; i < N; ++i) {
        Node* node = malloc(sizeof(Node));
        /* TODO: Better prng */
        srand(r);
        node->data = r = rand() % 100;
        if (head == NULL) {
            head = tail = node;
        }
        else {
            tail->next = node;
            tail = node;
            tail->next = NULL;
        }
    }

    printL(head);
    Node* L = msort(head);
    printL(L);

    Node* p = L;
    while (p != NULL) {
        Node* next = p->next;
        free(p);
        p = next;
    }
}
