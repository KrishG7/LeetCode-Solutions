class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # memo={}

        # def dfs(i,j):
        #     # Base Case 1: If j reaches the end of t, we successfully matched the whole string!
        #     if j == len(t):
        #         return 1

        #     # Base Case 2: If i reaches the end of s, but t isn't finished, this path failed.
        #     if i == len(s):
        #         return 0
            
        #     # Check the cache to see if we've already computed this exact state
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # Option 1: We always have the option to just skip s[i]
        #     res = dfs(i + 1, j)

        #     # Option 2: If the characters match, we ALSO have the option to use s[i]
        #     if s[i] == t[j]:
        #         res += dfs(i + 1, j + 1)
            
        #     # Save to cache before returning
        #     memo[(i, j)] = res
        #     return res
        
        # return dfs(0, 0)
        
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences matching t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty string 't' can always be formed 1 way
        
        for i in range(1, m + 1):
            # Iterate backwards through t to avoid overwriting data we still need
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
                    
        return dp[n]
