class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_final=nums[0]
        max_prev=0
        for i in range (len(nums)):
            if max_prev<0:
                max_prev=0
                
            max_prev+=nums[i]

            if max_prev>max_final:
                max_final=max_prev
        
        return max_final
