class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                if sum(path) == n:
                    res.append(list(path))
                return

            if sum(path) > n:
                return

            for i in range(start, 10):
                backtrack(i + 1, path + [i])

        backtrack(1, [])
        return res

