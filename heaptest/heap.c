
#include <stdio.h>
#include <stdlib.h>

struct Elem {
    int key;
    void* value;
};

#define HEAP_SIZE 100

struct Elem** _buf;
int _size;

void swap(int i, int j)
{
    struct Elem* temp = _buf[i];
    _buf[i] = _buf[j];
    _buf[j] = temp;
}

void heapify(int i)
{
    int p = (i-1) >> 1; // (int)floor((i-1)/2);

    int l = (i << 1) + 1; // 2 * i + 1
    int r = (i << 1) + 2; // 2 * i + 2

    struct Elem* e = _buf[i];

    if (i != 0) { // parent check
        struct Elem* parent = _buf[p];
        if (e->key < parent->key) {
            swap(i, p);
            heapify(p);
        }
    }

    if (_size >= l) { // child check
        if (_size <= r) { // only have left
            struct Elem* left = _buf[l];
            if (e->key > left->key) {
                swap(i, l);
                heapify(l);
            }
        }
        else { // have left and right
            struct Elem* left = _buf[l];
            struct Elem* right = _buf[r];
            int s = left->key < right->key ? l : r;
            struct Elem* child = _buf[s];
            if (e->key > child->key) {
                swap(i, s);
                heapify(s);
            }
        }
    }
}

void init()
{
    _buf = calloc(HEAP_SIZE, sizeof(struct Elem));
    _size = 0;
}

void uninit()
{
    for (int i = 0; i < _size; ++i) {
        free(_buf[i]);
    }
    free(_buf);
}

struct Elem* findMin()
{
    return _buf[0];
}

struct Elem* extractMin()
{
    struct Elem* min = findMin();
    _buf[0] = _buf[_size-1];
    _size -= 1;
    heapify(0);

    return min;
}

void insert(int key, void* value)
{
    struct Elem* elem = malloc(sizeof(struct Elem));
    elem->key = key;
    elem->value = value;
    _buf[_size] = elem;
    heapify(_size);
    _size += 1;
}

void changeKey(int index, int newKey)
{
    _buf[index]->key = newKey;
    heapify(index);
}

void printheap()
{
    for (int i = 0; i < _size; ++i) {
        int* pVal = _buf[i]->value;
        printf("(%d => %d), ", _buf[i]->key, *pVal);
    }
    printf("\n");
}

int main(int argc, char* argv[])
{
    int val = 1;

    init();

    insert(2, &val);
    printheap();

    insert(2, &val);
    printheap();

    insert(13, &val);
    printheap();

    insert(7, &val);
    printheap();

    insert(3, &val);
    printheap();

    insert(-1, &val);
    printheap();

    printf("Change Key\n");
    changeKey(0, 14);
    printheap();

    insert(77, &val);
    printheap();

    insert(8, &val);
    printheap();

    insert(0, &val);
    printheap();

    int items = _size;
    for (int i = 0; i < items; ++i) {
        struct Elem* e = extractMin();
        printf("Extract Min: %d\n", e->key);
        printheap();
    }

    uninit();

    return 0;
}
