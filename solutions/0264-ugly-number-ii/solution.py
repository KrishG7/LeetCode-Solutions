class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        p2 = p3 = p4 = 0

        for i in range(1, n):
            next2 = ugly[p2] * 2
            next3 = ugly[p3] * 3
            next4 = ugly[p4] * 5

            ugly[i] = min(next2, next3, next4)

            if ugly[i] == next2:
                p2 += 1

            if ugly[i] == next3:
                p3 += 1

            if ugly[i] == next4:
                p4 += 1

        return ugly[-1]

