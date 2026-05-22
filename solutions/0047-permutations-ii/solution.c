/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */
void swap(int* num, int* num2) {
    int temp;
    temp = *num;
    *num = *num2;
    *num2 = temp;
}

void reverse(int* nums, int start, int end) {
    while (start < end) {
        swap(&nums[start], &nums[end]);
        start++;
        end--;
    }
}

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int maxPerms = 40320; 
    int** result = (int**)malloc(maxPerms * sizeof(int*));
    *returnColumnSizes = (int*)malloc(maxPerms * sizeof(int));
    

    qsort(nums, numsSize, sizeof(int), cmp);
    
    int k = 0;
    
    while (1) {
        result[k] = (int*)malloc(numsSize * sizeof(int));
        for (int x = 0; x < numsSize; x++) {
            result[k][x] = nums[x];
        }
        (*returnColumnSizes)[k] = numsSize;
        k++; 
        
        int i = numsSize - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
 
        if (i < 0) {
            break; 
        }
        
        int j = numsSize - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        
        swap(&nums[i], &nums[j]);
        reverse(nums, i + 1, numsSize - 1);
    }
    
    *returnSize = k;
    return result;
}


