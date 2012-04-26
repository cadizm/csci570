
CC = gcc
CFLAGS = -Wall -std=c99
SRC = unionfind.c
OBJ = unionfind.o

all: unionfind

heap: $(OBJ)
	$(CC) -o unionfind $(OBJ)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC)

clean:
	rm -f unionfind $(OBJ)
