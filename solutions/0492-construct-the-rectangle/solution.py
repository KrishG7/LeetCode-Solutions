class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        w = int(math.isqrt(area))

        while area % w != 0:
            w -= 1

        return [area // w, w]

        # areas = []
        # for i in range(1, area + 1):
        #     path = []
        #     if area % i == 0:
        #         l = i
        #         w = area // i
        #         if l >= w:
        #             areas.append([l, w])

        # smallest = float("inf")
        # res = []
        # for l, w in areas:
        #     diff = l - w
        #     if diff <= smallest:
        #         smallest = diff
        #         res = [l, w]

        # return res

