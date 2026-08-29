#include <string.h>

void printRevWord(char *str, int s, int e) {
    int len = (e - s)/2;
    printf("%d \n", e); int count = 1;
    for (int i=s; i<=s+len-1; i++) {
        printf("%c - %c, %d - %d\n", str[i], str[e-count], i, e-count);
        char temp = str[i];
        str[i] = str[e-count];
        str[e-count] = temp;
        count += 1;
        // printf("%c", str[i]);
    }
    // printf("\n");
}
char* reverseWords(char* s) {
    int len = strlen(s), start = 0;
    for (int i=0; i<len+1; i++) {
        if (s[i] == ' ' || s[i] == '\0') {
            printRevWord(s, start, i);
            start = i+1;
        }
    }
    return s;
}