/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    *returnSize = ASize;
    int* C = (int*)malloc(ASize * sizeof(int));
    int* counts = (int*)calloc(ASize + 1, sizeof(int));

    int common_elements = 0;

    for (int i = 0; i < ASize; i++) {
        counts[A[i]]++;
        if (counts[A[i]] == 2) {
            common_elements++;
        }

        counts[B[i]]++;
        if (counts[B[i]] == 2) {
            common_elements++;
        }
        C[i] = common_elements;
    }
    return C;
}
