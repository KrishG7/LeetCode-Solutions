class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def helper(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]

            pick_left = nums[i] - helper(i + 1, j)
            pick_right = nums[j] - helper(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return helper(0, len(nums) - 1) >= 0

