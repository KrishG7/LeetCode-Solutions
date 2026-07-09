class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == len(set(nums)):
            return False

        for i in range (len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False

        # seen = {}

        # for i, num in enumerate(nums):
        #     # If we have seen the number and the index distance is <= k
        #     if num in seen and i - seen[num] <= k:
        #         return True
            
        #     # Update the latest index for this number
        #     seen[num] = i
            
        # return False
