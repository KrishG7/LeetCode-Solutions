class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        "Pythonic Optimisation"
        bulls = 0
        secret_counts = Counter()
        guess_counts = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] += 1
                guess_counts[g] += 1

        cows = sum(
            min(secret_counts[digit], guess_counts[digit]) for digit in secret_counts
        )

        return f"{bulls}A{cows}B"

        # bulls = 0
        # cows = 0

        # secret_count = [0] * 10
        # guess_count = [0] * 10

        # for s, g in zip(secret, guess):
        #     if s == g:
        #         bulls += 1
        #     else:
        #         secret_count[int(s)] += 1
        #         guess_count[int(g)] += 1

        # for i in range(10):
        #     cows += min(secret_count[i], guess_count[i])

        # return f"{bulls}A{cows}B"

