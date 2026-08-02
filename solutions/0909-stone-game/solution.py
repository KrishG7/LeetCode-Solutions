class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        # n = len(piles)
        # dp = list(piles)  # Base case for length 1
        
        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1
        #         dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])
                
        # return dp[0] >= 0

        "Longer Execution using recursion"
        # memo = {}

        # def helper(i, j):
        #     if i == j:
        #         return piles[i]
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     pick_left = piles[i] - helper(i + 1, j)
        #     pick_right = piles[j] - helper(i, j - 1)

        #     memo[(i, j)] = max(pick_left, pick_right)
        #     return memo[(i, j)]

        # return helper(0, len(piles) - 1) >= 0

