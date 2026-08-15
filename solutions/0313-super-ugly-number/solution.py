class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1

        k = len(primes)
        # indices[j] represents the index in dp that primes[j] will multiply to form its next candidate number.
        indices = [0] * k

        for i in range(1, n):
            next_ugly = min(primes[j] * dp[indices[j]] for j in range(k))
            dp[i] = next_ugly

            for j in range(k):
                if primes[j] * dp[indices[j]] == next_ugly:
                    indices[j] += 1

        return dp[-1]

