class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick length check
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: we successfully used all characters
            if i == len(s1) and j == len(s2):
                return True
            
            res = False
            # Current character in s3 we need to match is s3[i + j]
            target = s3[i + j]
            
            # Try s1
            if i < len(s1) and s1[i] == target:
                res = helper(i + 1, j)
            
            # Try s2 (only if we didn't find a path with s1)
            if not res and j < len(s2) and s2[j] == target:
                res = helper(i, j + 1)
                
            memo[(i, j)] = res
            return res

        return helper(0, 0)
