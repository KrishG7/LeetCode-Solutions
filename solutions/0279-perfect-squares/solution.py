class Solution:
    def numSquares(self, n: int) -> int:
        " every natural number can be represented as the sum of four or fewer integer squares "
        # Check if it is perfect square
        isqrt = math.isqrt(n)
        if isqrt * isqrt == n:
            return 1

        # 2. Check if it can be represented as 4^k * (8m + 7)
        temp = n
        while temp % 4 == 0:
            temp //= 4
        if temp % 8 == 7:
            return 4

        # 3. Check if it can be formed by 2 squares
        for i in range(1, math.isqrt(n) + 1):
            rem = n - i * i
            s = math.isqrt(rem)
            if s * s == rem:
                return 2

        return 3


        "Dp based solution"
        # dp = [i for i in range(n + 1)]
        
        # for i in range(1, n + 1):
        #     j = 1
        #     while j * j <= i:
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        #         j += 1
                
        # return dp[n]

