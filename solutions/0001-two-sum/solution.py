class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        j = 0
        i = 1
        
        while j < len(nums) - 1:
            if nums[j] + nums[i] == target:
                return [j, i]
            
            # If i reaches the end, advance j and restart i right after j
            if i == len(nums) - 1:
                j += 1
                i = j + 1
            else:
                i += 1
