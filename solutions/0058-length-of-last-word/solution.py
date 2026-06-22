class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1=s.split()
        return len(list1[-1])
        
