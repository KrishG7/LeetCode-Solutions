#define MAX_QUEUE_SIZE 100005

typedef struct {
    char* word;
    int level;
} Node;

int compareStrings(const void* a, const void* b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

int binarySearch(char** wordList, int size, const char* target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int cmp = strcmp(wordList[mid], target);
        if (cmp == 0)
            return mid;
        if (cmp < 0)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int ladderLength(char* beginWord, char* endWord, char** wordList,
                 int wordListSize) {
    int endWordIdx = -1;
    for (int i = 0; i < wordListSize; i++) {
        if (strcmp(wordList[i], endWord) == 0) {
            endWordIdx = i;
            break;
        }
    }
    if (endWordIdx == -1)
        return 0;

    qsort(wordList, wordListSize, sizeof(char*), compareStrings);

    int* visited = (int*)calloc(wordListSize, sizeof(int));
    Node* queue = (Node*)malloc(MAX_QUEUE_SIZE * sizeof(Node));
    int front = 0, rear = 0;

    queue[rear++] = (Node){beginWord, 1};

    int len = strlen(beginWord);

    while (front < rear) {
        Node current = queue[front++];

        if (strcmp(current.word, endWord) == 0) {
            free(visited);
            free(queue);
            return current.level;
        }

        char* curr_word = strdup(current.word);

        for (int i = 0; i < len; i++) {
            char original_char = curr_word[i];

            for (char c = 'a'; c <= 'z'; c++) {
                if (c == original_char)
                    continue;

                curr_word[i] = c;

                int j = binarySearch(wordList, wordListSize, curr_word);
                if (j != -1 && !visited[j]) {
                    visited[j] = 1;
                    queue[rear++] = (Node){wordList[j], current.level + 1};
                }
            }
            curr_word[i] = original_char;
        }
        free(curr_word);
    }

    free(visited);
    free(queue);
    return 0;
}
