class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        low, high = 0, (m * n) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_element = matrix[mid // n][mid % n]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
