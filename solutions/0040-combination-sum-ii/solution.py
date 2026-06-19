class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remaining, path, start):
            if remaining == 0:
                result.append(list(path))
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(remaining - candidates[i], path, i + 1)
                path.pop()

        backtrack(target, [], 0)
        return result

