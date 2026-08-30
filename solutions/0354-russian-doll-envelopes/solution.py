class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []

        for _, h in envelopes:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)

        # tails = []
        # for _, h in envelopes:
        #     left, right = 0, len(tails)

        #     while left < right:
        #         mid = (left + right) // 2
        #         if tails[mid] < h:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     if left == len(tails):
        #         tails.append(h)
        #     else:
        #         tails[left] = h

        # return len(tails)

