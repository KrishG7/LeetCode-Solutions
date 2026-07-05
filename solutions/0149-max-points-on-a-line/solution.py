class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 1

        for i in range(len(points)):
            p1 = points[i]
            # If you use a normal dictionary (slopes = {}) and try to update a slope you haven't seen yet (slopes[slope] += 1), Python will instantly crash with a KeyError
            # By using collections.defaultdict(int), you are telling Python: "If I ask for a key that doesn't exist, don't crash. Just instantly create it and set its default value to 0."

            slopes = collections.defaultdict(int)

            for j in range(i + 1, len(points)):
                p2 = points[j]

                dy = p2[1] - p1[1]
                dx = p2[0] - p1[0]

                if dx == 0:
                    slope = float("inf")
                else:
                    slope = dy / dx

                slopes[slope] += 1
                # Update our global max (adding 1 to include the anchor point p1)
                max_points = max(max_points, slopes[slope] + 1)
        return max_points

