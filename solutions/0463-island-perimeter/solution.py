class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    count+=4
                    if c + 1 < cols and grid[r][c + 1] == 1:
                        count -= 1
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        count -= 1
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        count -= 1
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        count -= 1
            
        return count
