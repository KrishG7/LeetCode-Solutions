class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for char in columnTitle:
            # Multiply the current total by 26 to shift it left, 
            # then add the 1-26 integer value of the new character!
            count = (count * 26) + (ord(char) - 64)
            
        return count

