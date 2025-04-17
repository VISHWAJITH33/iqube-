#include <stdio.h>

void reverseString(char* s, int sSize);

int main() {
    char s[] = {'h','e','l','l','o'};
    int size = sizeof(s)/sizeof(s[0]);

    reverseString(s, size);

    for (int i = 0; i < size; i++) {
        printf("%c ", s[i]);
    }

    return 0;
}
