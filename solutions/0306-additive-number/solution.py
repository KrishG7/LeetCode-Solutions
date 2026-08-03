class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        for i in range(1, n - 1):
            # First number cannot have leading zeros unless its just 0
            if num[0] == "0" and i > 1:
                break
            for j in range(i + 1, n):
                # Second number cannot have leading zeros unless its just 0
                if num[i] == "0" and j - i > 1:
                    break

                n1_str, n2_str = num[:i], num[i:j]
                n1, n2 = int(n1_str), int(n2_str)

                if self.isValid(n1, n2, num[j:]):
                    return True

        return False

    def isValid(self, n1: int, n2: int, remaining: str) -> bool:
        if not remaining:
            return True

        n3 = n1 + n2
        n3_str = str(n3)

        if not remaining.startswith(n3_str):
            return False

        return self.isValid(n2, n3, remaining[len(n3_str) :])

