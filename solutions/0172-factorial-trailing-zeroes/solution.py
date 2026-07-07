class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0

        # How do you get a trailing zero? You multiply by 10.
        # What makes a 10? A 2 multiplied by a 5.
        # If you look at all the numbers in a factorial (e.g., 1 * 2 * 3 * 4 * 5 * 6...), there are way more even numbers (2s) than there are 5s. That means the number of 5s determines exactly how many trailing zeros we get!
        # If you want to know how many numbers in that sequence are multiples of 5, you just do 11 // 5.
        # 11 // 5 = 2.
        # It instantly tells you there are exactly 2 multiples of 5 (which are 5 and 10). No loops, no modulo, just instant counting!
        while n > 0:
            n //= 5
            zero_count += n

        return zero_count

