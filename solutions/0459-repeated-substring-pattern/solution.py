class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        "If you take a string s, concatenate it with itself (s + s), remove the very first and very last character, and s can be formed by repeating a substring, then s will still appear somewhere inside that modified string"
        return s in (s + s)[1:-1]


        "The Substring Length Approach:"       
        # n = len(s)
        # for i in range(1, n // 2 + 1):
        #     if n % i == 0:
        #         substring = s[:i]
        #         if substring * (n // i) == s:
        #             return True
        # return False

        "Using Sliding Window:"
        # n = len(s)

        # for i in range(n // 2):
        #     window_len = i + 1

        #     if n % window_len == 0:
        #         window = s[:window_len]

        #         is_valid = True
        #         for j in range(window_len, n, window_len):
        #             if s[j : j + window_len] != window:
        #                 is_valid = False
        #                 break

        #         if is_valid:
        #             return True

        # return False

