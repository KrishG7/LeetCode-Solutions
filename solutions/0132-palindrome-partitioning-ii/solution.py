class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_pal[i][j] is True if s[i...j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        # dp[i] stores the minimum cuts needed for s[0...i]
        dp = [0] * n

        for i in range(n):
            # Worst case baseline: we cut every single character (e.g., length 3 needs 2 cuts)
            min_cuts = i

            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True

                    # If the entire prefix s[0...i] is a palindrome, we don't need any cuts!
                    if j == 0:
                        min_cuts = 0
                    else:
                        # Otherwise, make a cut before j. 
                        # Total cuts = (cuts needed for the prefix before j) + 1
                        min_cuts = min(min_cuts, dp[j - 1] + 1)

            dp[i] = min_cuts

        return dp[n - 1]

