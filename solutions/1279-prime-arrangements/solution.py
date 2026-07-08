class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(num):
            if num < 2: return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0: return False
            return True
        
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count
        
        # 2. Result is (prime_count! * non_prime_count!) % (10^9 + 7)
        MOD = 10**9 + 7
        return (math.factorial(prime_count) * math.factorial(non_prime_count)) % MOD
