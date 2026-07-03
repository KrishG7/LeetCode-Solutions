class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=[]
        for char in s:
            if char.isalnum():
                r.append(char.lower())
        return r==r[::-1]
        # # 1. Set pointers to the true beginning and end of the string
        # left = 0
        # right = len(s) - 1
        
        # while left < right:
        #     # 2. Skip over any non-alphanumeric characters from the left
        #     while left < right and not s[left].isalnum():
        #         left += 1
                
        #     # 3. Skip over any non-alphanumeric characters from the right
        #     while left < right and not s[right].isalnum():
        #         right -= 1
                
        #     # 4. Compare the valid characters (force them to lowercase first)
        #     if s[left].lower() != s[right].lower():
        #         return False
            
        #     # 5. Move pointers inward to check the next pair!
        #     left += 1
        #     right -= 1
            
        # return True
