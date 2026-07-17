class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
        # count = [0] * 26

        # for char in magazine:
        #     count[ord(char) - ord("a")] += 1

        # for char in ransomNote:
        #     index = ord(char) - ord("a")
        #     count[index] -= 1

        #     if count[index] < 0:
        #         return False

        # return True

