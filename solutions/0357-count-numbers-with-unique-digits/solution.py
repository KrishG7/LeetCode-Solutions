class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        unique_digits_product = 9
        available_choices = 9

        for _ in range(2, n + 1):
            unique_digits_product *= available_choices
            total += unique_digits_product
            available_choices -= 1

        return total

