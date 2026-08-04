class Solution:
    def maxProduct(self, n: int) -> int:
        # digits = sorted([int(char) for char in str(n)])
        # return digits[-1] * digits[-2]

        digits = [int(char) for char in str(n)]
        max1 = max(digits)
        digits.remove(max1)
        max2 = max(digits)
        return max1 * max2

