
CC = gcc
CFLAGS = -Wall -std=c99
SRC = heap.c
OBJ = heap.o

all: heap

heap: $(OBJ)
	$(CC) -o heap $(OBJ)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC)

clean:
	rm -f heap $(OBJ)
