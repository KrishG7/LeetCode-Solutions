bool canJump(int* nums, int numsSize) {
    int farthest = 0;
    for (int i = 0; i < numsSize; i++) {
        if (farthest < i)
            return false;
        farthest = (farthest > i + nums[i]) ? farthest : (i + nums[i]);
        if (farthest >= numsSize - 1) {
            return true;
        }
    }
    return false;
}
