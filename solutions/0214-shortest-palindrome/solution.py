class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # if s == s[::-1]:
        #     return s

        # b = len(s)
        # while b > 0:
        #     if s[:b] == s[:b][::-1]:
        #         break
        #     b -= 1

        # return s[b:][::-1] + s

        i, n = 0, len(s)
        for c in s[::-1]:
            if c == s[i]:
                i += 1
        if i == n:
            return s
        sub = s[i:]
        return sub[::-1] + self.shortestPalindrome(s[0:i]) + sub
       

