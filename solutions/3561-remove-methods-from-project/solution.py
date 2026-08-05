class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)

        suspicious = set([k])
        queue = deque([k])

        while queue:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                if neighbour not in suspicious:
                    suspicious.add(neighbour)
                    queue.append(neighbour)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        return [i for i in range(n) if i not in suspicious]

