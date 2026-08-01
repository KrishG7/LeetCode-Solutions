class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        count = Counter(nums)
        for num, freq in count.items():
            if freq > n // 3:
                res.append(num)
        return res

