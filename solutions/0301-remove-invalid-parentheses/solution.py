class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        queue = [s]
        visited = {s}

        while queue:
            level_size = len(queue)
            level_nodes = []
            res = []
            found = False

            for _ in range(level_size):
                curr = queue.pop(0)
                level_nodes.append(curr)

                if isValid(curr):
                    res.append(curr)
                    found = True

            if found:
                return res

            for curr in level_nodes:
                for i in range(len(curr)):
                    if curr[i] not in ('(', ')'):
                        continue
                    next_str = curr[:i] + curr[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

        return [""]
