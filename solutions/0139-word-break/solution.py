class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False] * (len(s)+1)

        # Base case: an empty string is always a valid starting point
        dp[0]=True

        for i in range(len(s)):
            if dp[i]:
                for w in wordDict:
                    if s[i:i+len(w)]==w:
                        # Place a new checkpoint at the end of this word
                        dp[i+len(w)]=True
                    
        return dp[len(s)]
