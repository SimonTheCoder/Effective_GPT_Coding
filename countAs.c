#include <stdio.h>

int countAs(char* str) {
    int count = 0;
    
    while (*str != '\0') {
        if (*str == 'A' || *str == 'a') {
            count++;
        }
        str++;
    }
    
    return count;
}

int main() {
    char* input = "An apple a day keeps the doctor away.";
    int result = countAs(input);
    
    printf("Number of 'A's: %d\n", result);
    
    return 0;
}