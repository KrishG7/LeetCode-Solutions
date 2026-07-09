class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))

        # if len(s) != len(t):
        #     return False
        # s_to_t = {}
        # t_taken = set()
        # for i in range(len(s)):
        #     char_s = s[i]
        #     char_t = t[i]

        #     if char_s in s_to_t:
        #         # If we've seen this s-char, it must map to the same t-char
        #         if s_to_t[char_s] != char_t:
        #             return False
        #     else:
        #         # If this s-char is new, t-char must not be taken by another s-char
        #         if char_t in t_taken:
        #             return False

        #         s_to_t[char_s] = char_t
        #         t_taken.add(char_t)

        # return True

