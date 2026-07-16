class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        return 1 + (num - 1) % 9

        # if num < 10:
        #     return num
        # sum_num = 0
        # sum_num += num % 10
        # num //= 10
        # sum_num += num
        # number=str(sum_num)
        # if len(number) > 1:
        #     return self.addDigits(sum_num)
        # return sum_num

