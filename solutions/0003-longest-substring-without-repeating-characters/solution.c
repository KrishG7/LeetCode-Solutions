#include <string.h>
int lengthOfLongestSubstring(char* s) {
    int seq=0;
    int len=strlen(s);

    int lastIndex[128];
    for (int i = 0; i < 128; i++) {
        lastIndex[i] = -1;
    }
    int start=0;
    for (int end=0;end<len;end++){
        char currentChar=s[end];
        if (lastIndex[currentChar]>=start){
            start=lastIndex[currentChar] + 1;
        }
        lastIndex[currentChar]=end;
        int currentLength = end - start + 1;
        if (currentLength > seq) {
            seq = currentLength;
        }
    }

    return seq;
}

