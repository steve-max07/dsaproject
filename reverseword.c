#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 1000

// Define the Stack Structure
char stack[MAX_SIZE];
int top = -1;

// Push operation: Adds a character to the top of the stack
void push(char ch) {
    if (top < MAX_SIZE - 1) {
        stack[++top] = ch;
    }
}

// Pop operation: Removes and returns the top character from the stack
char pop() {
    if (top >= 0) {
        return stack[top--];
    }
    return '\0'; // Return null character if stack is empty
}

int main(int argc, char *argv[]) {
    // Check if a word was passed as a command-line argument from the backend
    if (argc < 2) {
        printf("Error: No word provided.");
        return 1;
    }

    // argv[1] contains the word sent by the user through the webpage
    char *word = argv[1];
    int length = strlen(word);

    // 1. Push all characters of the word onto the stack (LIFO arrangement)
    for (int i = 0; i < length; i++) {
        push(word[i]);
    }

    // 2. Pop all characters off the stack to print them in reverse order
    for (int i = 0; i < length; i++) {
        printf("%c", pop());
    }

    return 0;
}