class Solution:
    def arrangeCoins(self, n: int) -> int:

        # The total number of coins needed to build k complete rows is given by the formula:{k(k + 1)}/{2} <=n .
        # We can rearrange this quadratic equation using the quadratic formula (ax^2 + bx + c = 0) to solve directly for k:
        # k = floor(sqrt(2n + {1}/{4}) - {1}/{2})

        return int(math.isqrt(8 * n + 1) - 1) // 2

        # s = 1
        # sum_n = 0

        # while sum_n + s <= n:
        #     sum_n += s
        #     s += 1

        # return s - 1

