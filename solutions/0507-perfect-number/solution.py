class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total_sum = 1

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total_sum += i

                if i != num // i:
                    total_sum += (num // i)

        return total_sum == num

        "TLE:"
        # nums = []
        # for i in range(1, (num // 2) + 1):
        #     if num % i == 0:
        #         nums.append(i)

        # if sum(nums) == num:
        #     return True
        # return False

