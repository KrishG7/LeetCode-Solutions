class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)

        return n == 1

    def sumOfSquares(self, n):
        output = 0
        while n > 0:
            digit = n % 10
            output += digit * digit
            n //= 10
        return output

