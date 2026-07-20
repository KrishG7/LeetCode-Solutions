class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_time = 0
        n = len(timeSeries)

        for i in range(n - 1):
            total_time += min(duration, timeSeries[i + 1] - timeSeries[i])

        total_time += duration

        return total_time

