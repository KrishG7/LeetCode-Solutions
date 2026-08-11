class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + [x for x in nums if x > 0] + [1]
        n = len(balloons)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                # Try setting every balloon `k` between `i` and `j` as the last balloon to burst in interval (i, j)
                for k in range(i + 1, j):
                    # Coins from bursting `k` last = coins from left subproblem + coins from right subproblem + coins from bursting k
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + balloons[i] * balloons[k] * balloons[j],
                    )

        return dp[0][n - 1]

