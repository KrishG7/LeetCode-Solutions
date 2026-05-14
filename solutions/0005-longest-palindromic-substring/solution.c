#include <stdlib.h>
#include <string.h>

int expand(char* s, int left, int right, int n) {
    while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

char* longestPalindrome(char* s) {
    int n = strlen(s);
    if (n < 1)
        return "";
    int start = 0;
    int maxlen = 0;
    for (int i = 0; i < n; i++) {
        int len1 = expand(s, i, i, n);
        int len2 = expand(s, i, i + 1, n);
        int len = (len1 > len2) ? len1 : len2;

        if (len > maxlen) {
            maxlen = len;
            start = i - (len - 1) / 2;
        }
    }
    char* result = (char*)malloc((maxlen + 1) * sizeof(char));
    strncpy(result, s + start, maxlen);
    result[maxlen] = '\0';

    return result;
}
