int maxSubArray(int* nums, int numsSize) {
    int max_num=nums[0];
    int max_prev=0;
    for(int i=0;i<numsSize;i++){
        if(max_prev<0){
            max_prev=0;
        }
        max_prev+=nums[i];
        if(max_prev>max_num){
            max_num=max_prev;
        }
    }
    return max_num;
}
