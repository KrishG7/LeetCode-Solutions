class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_num_product(num: int) -> int:
            pro = 1
            for d in str(num):
                pro *= int(d)
            return pro

        curr = n
        while True:
            if get_num_product(curr) % t == 0:
                return curr
            curr += 1

