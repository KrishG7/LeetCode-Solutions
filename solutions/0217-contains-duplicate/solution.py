class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # check = set()
        # for i in range(len(nums)):
        #     if nums[i] in check:
        #         return True
        #     else:
        #         check.add(nums[i])
        # return False

