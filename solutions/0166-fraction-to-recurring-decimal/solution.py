class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        num = abs(numerator)
        den = abs(denominator)

        res.append(str(num // den))
        rem = num % den

        if rem == 0:
            return "".join(res)

        res.append(".")

        seen_remainders = {}

        while rem != 0:
            if rem in seen_remainders:
                res.insert(seen_remainders[rem], "(")
                res.append(")")
                break

            seen_remainders[rem] = len(res)

            rem *= 10
            res.append(str(rem // den))
            rem %= den

        return "".join(res)

