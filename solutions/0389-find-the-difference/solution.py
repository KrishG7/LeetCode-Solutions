class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = sum(ord(char) for char in t) - sum(ord(char) for char in s)
        return chr(diff)
