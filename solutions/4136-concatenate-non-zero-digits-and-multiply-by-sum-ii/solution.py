class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Precompute arrays
        sum_d = [0] * (n + 1)
        val_concat = [0] * (n + 1)
        len_concat = [0] * (n + 1)
        
        # Precompute powers for O(1) weight calculation
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # Single loop to build all prefix data
        for i, char in enumerate(s):
            digit = int(char)
            sum_d[i + 1] = sum_d[i] + digit
            
            if digit != 0:
                val_concat[i + 1] = (val_concat[i] * 10 + digit) % MOD
                len_concat[i + 1] = len_concat[i] + 1
            else:
                val_concat[i + 1] = val_concat[i]
                len_concat[i + 1] = len_concat[i]
        
        results = []
        for l, r in queries:
            # 1. Total sum of digits in range [l, r]
            sd = sum_d[r + 1] - sum_d[l]
            
            # 2. Number of non-zero digits in range [l, r]
            cnt = len_concat[r + 1] - len_concat[l]
            
            if cnt == 0:
                results.append(0)
                continue
            
            # 3. Concatenated value 'x' in range [l, r]
            # Formula: (Full_Concat[r] - Full_Concat[l-1] * 10^cnt_in_range)
            # Since our arrays are 1-indexed, it uses l and r+1
            x = (val_concat[r + 1] - val_concat[l] * pow10[cnt]) % MOD
            x = (x + MOD) % MOD # Handle negative result from modulo
            
            results.append((x * sd) % MOD)
            
        return results

        
        # TLE:
        # MOD = 10**9 + 7
        # n = len(s)

        # pref_sum = [0] * (n + 1)

        # non_zero_indices = []

        # for i in range(n):
        #     digit = int(s[i])
        #     pref_sum[i + 1] = pref_sum[i] + digit
        #     if digit != 0:
        #         non_zero_indices.append(i)

        # powers = [1] * (n + 1)
        # for i in range(1, n + 1):
        #     powers[i] = (powers[i - 1] * 10) % MOD

        # results = []

        # for start, end in queries:
        #     left_idx = bisect_left(non_zero_indices, start)
        #     right_idx = bisect_right(non_zero_indices, end)

        #     subset_indices = non_zero_indices[left_idx:right_idx]

        #     if not subset_indices:
        #         results.append(0)
        #         continue

        #     x = 0
        #     k = len(subset_indices)
        #     for i in range(k):
        #         digit = int(s[subset_indices[i]])
        #         weight = powers[k - 1 - i]
        #         x = (x + digit * weight) % MOD

        #     sum_num = pref_sum[end + 1] - pref_sum[start]

        #     results.append((x * sum_num) % MOD)
        # return results

        # Failed on larger inputs:
        # res = []
        # for start, end in queries:
        #     a = []
        #     for i in range(start, end + 1):
        #         if s[i] != "0":
        #             a.append(s[i])

        #     if not a:
        #         res.append(0)
        #     else:
        #         x = int("".join(a))
        #         sum_num = sum(int(digit) for digit in a)
        #         res.append((x * sum_num) % (10**9 + 7))
        # return res

