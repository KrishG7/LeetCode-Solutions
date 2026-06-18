/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* range = (int*)malloc(2 * sizeof(int));
    range[0] = -1;
    range[1] = -1;
    *returnSize = 2;

    int left = 0;
    int right = numsSize - 1;
    if (numsSize == 0)
        return range;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] >= target) {
            if (nums[mid] == target) {
                range[0] = mid;
            }
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    left = 0;
    right = numsSize - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            if (nums[mid] == target) {
                range[1] = mid;
            }
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return range;
}
