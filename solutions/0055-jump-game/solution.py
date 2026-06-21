class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest=0
        last=len(nums)
        for i in range(last):
            if i>farthest:
                return False

            farthest=max(farthest,i+nums[i])

            if farthest>=len(nums)-1:
                return True
        
        return False
        
