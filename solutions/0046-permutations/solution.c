/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */

void backtrack(int* nums, int numsSize, int** result, int* returnIdx,
               int* currentPath, int* used, int depth) {
    if (depth == numsSize) {
        memcpy(result[*returnIdx], currentPath, numsSize * sizeof(int));
        (*returnIdx)++;
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        if (!used[i]) {
            used[i] = 1;
            currentPath[depth] = nums[i];

            backtrack(nums, numsSize, result, returnIdx, currentPath, used,
                      depth + 1);

            used[i] = 0;
        }
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    if (numsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int fac = 1;
    for (int i = 2; i <= numsSize; i++) {
        fac *= i;
    }

    *returnSize = fac;
    *returnColumnSizes = (int*)malloc(fac * sizeof(int));
    for (int i = 0; i < fac; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }
    int** result = (int**)malloc(fac * (sizeof(int*)));
    for (int i = 0; i < fac; i++) {
        result[i] = (int*)malloc(numsSize * sizeof(int));
    }
    int* used = (int*)calloc(numsSize, sizeof(int));
    int* currentPath = (int*)malloc(numsSize * sizeof(int));
    int returnIdx = 0;

    backtrack(nums, numsSize, result, &returnIdx, currentPath, used, 0);

    free(used);
    free(currentPath);

    return result;
}
