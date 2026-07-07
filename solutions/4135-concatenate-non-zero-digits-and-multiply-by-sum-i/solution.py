class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        a = []
        for char in s:
            if char != "0":
                a.append(char)
        
        if not a:
            return 0

        x = int("".join(a))
        sum_num = sum(int(digit) for digit in str(x))

        return x * sum_num

