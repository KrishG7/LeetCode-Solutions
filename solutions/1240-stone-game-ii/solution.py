class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            # Base Case: If remaining piles (n - i) are <= 2 * m,
            if i + 2 * m >= n:
                return suffix_sum[i]

            if (i, m) in memo:
                return memo[(i, m)]

            res = 0 # Track the maximum stones the current player can secure from index `i`

            # Explore all possible valid moves: take x piles where 1 <= x <= 2 * m
            for x in range(1, 2 * m + 1):
                # The total stones remaining from index i is suffix_sum[i].
                # The opponent will get dp(i + x, max(m, x)) from the next turn.
                # Therefore, current player gets: (Total remaining stones) - (Stones opponent will get).
                # We update `res` to maximize this value across all valid choices of x.
                res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))

            memo[(i, m)] = res
            return res

        return dp(0, 1)

