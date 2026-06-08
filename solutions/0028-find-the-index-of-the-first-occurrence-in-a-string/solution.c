int strStr(char* haystack, char* needle) {
    int len1 = strlen(haystack);
    int len2 = strlen(needle);

    if (len2 > len1)
        return -1;
        
    for (int i = 0; i <= len1 - len2; i++) {
        int j;

        for (j = 0; j < len2; j++) {
            if (haystack[i + j] != needle[j]) {
                break;
            }
        }

        if (j == len2) {
            return i;
        }
    }
    return -1;
}
