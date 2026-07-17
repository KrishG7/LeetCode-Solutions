class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_1 = len(nums1)
        len_2 = len(nums2)
        check = [0] * 1001
        res = []

        for i in range(len_1):
            check[nums1[i]] += 1

        for i in range(len_2):
            if check[nums2[i]] > 0:
                res.append(nums2[i])
                check[nums2[i]] -= 1

        return res

