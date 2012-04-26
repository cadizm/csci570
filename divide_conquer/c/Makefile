
CC = gcc
CFLAGS = -ggdb -Wall -std=c99
SRC = mergesort.c msort.c
OBJ = mergesort.o msort.o

all: mergesort msort

mergesort: $(OBJ)
	$(CC) mergesort.o -o mergesort

msort: $(OBJ)
	$(CC) msort.o -o msort

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC)

clean:
	rm -f mergesort msort $(OBJ)
