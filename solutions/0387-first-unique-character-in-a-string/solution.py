class Solution:
    def firstUniqChar(self, s: str) -> int:
        check={}

        for char in s:
            check[char] = check.get(char, 0) + 1
            # if char in check:
            #     check[char]+=1
            # else:
            #     check[char]=1
        
        for i in range(len(s)):
            if check[s[i]] == 1:
                return i
        
        return -1
