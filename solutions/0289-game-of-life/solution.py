class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # First Pass: Apply rules and encode with -1 and 2
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # Count if neighbor was originally alive (1 or marked as -1 dying)
                        if board[nr][nc] == 1 or board[nr][nc] == -1:
                            live_neighbors += 1

                # Conway's Rules
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Live -> Dead
                elif board[r][c] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                    pass  # Stays live
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Dead -> Live

        # Second Pass: Clean up into final 0s and 1s
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

