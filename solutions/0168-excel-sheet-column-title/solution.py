class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1

            rem = columnNumber % 26
            res.append(chr(rem + ord("A")))

            columnNumber //= 26

        return "".join(res[::-1])

