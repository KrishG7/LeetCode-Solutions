class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1. Convert all integers to strings for concatenation
        arr = [str(num) for num in nums]
        
        # 2. Define custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come first
            elif a + b < b + a:
                return 1   # b should come first
            else:
                return 0
        
        # 3. Sort using the custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # 4. Join and handle the edge case of "000" -> "0"
        if arr[0] == '0': return "0"
        return ''.join(arr)
