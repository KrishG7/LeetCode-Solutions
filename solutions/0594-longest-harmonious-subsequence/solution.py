class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for x in freq:
            if x + 1 in freq:
                max_len = max(max_len, freq[x] + freq[x + 1])

        return max_len

