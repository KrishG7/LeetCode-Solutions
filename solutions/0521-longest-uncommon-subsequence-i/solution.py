class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If two strings are completely identical, there is no uncommon subsequence, so it returns -1.
        # If two strings are different, the longer string can never be a subsequence of the shorter one. Therefore, the length of the longer string is always the answer.
        if a == b:
            return -1
        return max(len(a), len(b))

