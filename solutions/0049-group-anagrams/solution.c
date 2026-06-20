#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char* key;
    char** list;
    int size;
    int capacity;
    struct Node* next;
} Node;

// Generate a frequency key like "1#0#2#0...0#" for a string
char* generateKey(char* s) {
    int counts[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) counts[s[i] - 'a']++;
    char* key = (char*)malloc(100);
    int pos = 0;
    for (int i = 0; i < 26; i++) {
        pos += sprintf(key + pos, "%d#", counts[i]);
    }
    return key;
}

char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    Node* table[1000] = {NULL}; // Hash table buckets
    int groupCount = 0;

    for (int i = 0; i < strsSize; i++) {
        char* key = generateKey(strs[i]);
        int hash = 0;
        for (int j = 0; key[j] != '\0'; j++) hash = (hash * 31 + key[j]) % 1000;

        Node* curr = table[hash];
        while (curr != NULL && strcmp(curr->key, key) != 0) curr = curr->next;

        if (curr == NULL) {
            curr = (Node*)malloc(sizeof(Node));
            curr->key = key;
            curr->size = 0;
            curr->capacity = 10;
            curr->list = (char**)malloc(sizeof(char*) * 10);
            curr->next = table[hash];
            table[hash] = curr;
            groupCount++;
        } else {
            free(key);
        }

        if (curr->size == curr->capacity) {
            curr->capacity *= 2;
            curr->list = (char**)realloc(curr->list, sizeof(char*) * curr->capacity);
        }
        curr->list[curr->size++] = strs[i];
    }

    *returnSize = groupCount;
    *returnColumnSizes = (int*)malloc(sizeof(int) * groupCount);
    char*** result = (char***)malloc(sizeof(char**) * groupCount);

    int idx = 0;
    for (int i = 0; i < 1000; i++) {
        Node* curr = table[i];
        while (curr != NULL) {
            (*returnColumnSizes)[idx] = curr->size;
            result[idx] = curr->list;
            Node* temp = curr;
            curr = curr->next;
            free(temp->key);
            free(temp);
            idx++;
        }
    }
    return result;
}
