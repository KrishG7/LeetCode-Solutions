class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        arr = list(enumerate(nums))

        def merge_sort(enum_arr):
            if len(enum_arr) <= 1:
                return enum_arr

            mid = len(enum_arr) // 2
            left = merge_sort(enum_arr[:mid])
            right = merge_sort(enum_arr[mid:])

            merged = []
            i = j = 0
            right_counter = 0  # Number of smaller elements jumped from right half

            while i < len(left) and j < len(right):
                if right[j][1] < left[i][1]:
                    right_counter += 1
                    merged.append(right[j])
                    j += 1
                else:
                    counts[left[i][0]] += right_counter
                    merged.append(left[i])
                    i += 1

            while i < len(left):
                counts[left[i][0]] += right_counter
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)
        return counts

