class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        prev2 = 0
        prev1 = 1

        for i in range(1, len(s) + 1):
            curr = 0
            char = s[i - 1]

            if char == "*":
                curr = (prev1 * 9) % MOD
            elif char != "0":
                curr = prev1

            if i > 1:
                prev_char = s[i - 2]
                if prev_char == "*":
                    if char == "*":
                        curr = (curr + prev2 * 15) % MOD
                    elif char <= "6":
                        curr = (curr + prev2 * 2) % MOD
                    else:
                        curr = (curr + prev2) % MOD
                elif prev_char == "1":
                    if char == "*":
                        curr = (curr + prev2 * 9) % MOD
                    else:
                        curr = (curr + prev2) % MOD
                elif prev_char == "2":
                    if char == "*":
                        curr = (curr + prev2 * 6) % MOD
                    elif char <= "6":
                        curr = (curr + prev2) % MOD

            prev2, prev1 = prev1, curr

        return prev1

