class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_count = 0
        t_count = 0

        while s_count < len(s) and t_count < len(t):
            if s[s_count] != t[t_count]:
                t_count += 1
            else:
                s_count += 1
                t_count += 1

        if s_count == len(s):
            return True

        return False

