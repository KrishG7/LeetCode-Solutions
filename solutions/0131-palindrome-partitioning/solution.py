class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return res

