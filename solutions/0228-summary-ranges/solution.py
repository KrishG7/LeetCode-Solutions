class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            # Keep moving forward while the next number is consecutive
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            # Now nums[i] is the end of the range
            if start == nums[i]:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{nums[i]}")
            
            i += 1
            
        return res
