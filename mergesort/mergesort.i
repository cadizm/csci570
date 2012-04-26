
/* mergesort.i */

%module mergesort
%{
    extern int* mergesort(int* L, int len);
%}


extern int* mergesort(int* L, int len);
