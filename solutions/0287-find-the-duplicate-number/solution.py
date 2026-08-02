class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [False] * len(nums)

        for i in nums:
            if arr[i]:
                return i
            arr[i] = True

        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow

