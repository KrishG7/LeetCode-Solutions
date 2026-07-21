class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)
        res = []

        while num > 0:
            quotient = num % 7
            num //= 7
            res.append(str(quotient))

        result_str = "".join(res[::-1])
        return "-" + result_str if is_negative else result_str

