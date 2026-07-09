class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        comp = [0] * n
        current_comp = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_comp += 1
            comp[i] = current_comp

        res = []
        for u, v in queries:
            res.append(comp[u] == comp[v])
        return res

