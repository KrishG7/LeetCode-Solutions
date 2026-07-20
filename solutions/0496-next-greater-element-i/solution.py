class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_greater_map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater_map[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater_map[stack.pop()] = -1

        return [next_greater_map[x] for x in nums1]

        # res = []
        # i = 0

        # while i < len(nums1):
        #     target = nums1[i]
        #     idx = nums2.index(target)

        #     next_greater = -1
        #     for j in range(idx + 1, len(nums2)):
        #         if nums2[j] > target:
        #             next_greater = nums2[j]
        #             break

        #     res.append(next_greater)
        #     i += 1

        # return res

