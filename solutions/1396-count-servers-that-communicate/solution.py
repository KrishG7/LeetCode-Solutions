class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # row_count=[sum(row) for row in grid]
        # col_count=[sum(col) for col in zip(*grid)]

        # total=sum(row_count)

        # isolated=sum(
        #     1 for r, row in enumerate(grid)
        #     if row_count[r]==1 and col_count[row.index(1)]==1
        # )

        # return total-isolated

        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        last_col = [-1] * m
        total = 0
        
        # Pass 1: Find total servers and row/col counts
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    total += 1
                    row_count[r] += 1
                    col_count[c] += 1
                    last_col[r] = c
                    
        # Pass 2: Subtract isolated servers in O(m) time
        for r in range(m):
            if row_count[r] == 1 and col_count[last_col[r]] == 1:
                total -= 1
                
        return total
