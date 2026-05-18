/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */

 int compareFunc(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    int capacity = 20000;
    
    int** res = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));

    qsort(nums, numsSize, sizeof(int), compareFunc);
    
    for (int i = 0; i < numsSize - 2; i++) {
        if (i>0 && nums[i] == nums[i - 1]){
            continue;
        }
        
        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int current_sum = nums[i] + nums[left] + nums[right];
            if (current_sum == 0) {
                res[*returnSize] = (int*)malloc(3 * sizeof(int));
                res[*returnSize][0] = nums[i];
                res[*returnSize][1] = nums[left];
                res[*returnSize][2] = nums[right];

                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;

                left++;
                right--;

                while (left < right && nums[left] == nums[left - 1]) left++;
                while (left < right && nums[right] == nums[right + 1]) right--;
                }
            else if (current_sum < 0) left++;
            else right--;
        }
    }
    return res;
}
