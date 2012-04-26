
CC = gcc
CFLAGS = -Wall -std=c99
SRC = mergesort.c mergesort_wrap.c
OBJ = mergesort.o mergesort_wrap.o
INC = -I/usr/include/python2.4
LIBPATH = -L/usr/lib/python2.4/config
LIBS = -lpython2.4

all: gen mergesort

gen:
	swig -python mergesort.i

mergesort: $(OBJ)
	$(CC) -shared $(OBJ) $(LIBPATH) $(LIBS) -o _mergesort.dll

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC) $(INC)

clean:
	rm -f _mergesort.dll mergesort_wrap.c mergesort.py mergesort.pyc $(OBJ)
