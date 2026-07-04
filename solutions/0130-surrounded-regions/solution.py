class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def capture_safe(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return

            board[r][c] = "T"

            capture_safe(r + 1, c)
            capture_safe(r - 1, c)
            capture_safe(r, c + 1)
            capture_safe(r, c - 1)

        for r in range(rows):
            capture_safe(r, 0)
            capture_safe(r, cols - 1)

        for c in range(cols):
            capture_safe(0, c)
            capture_safe(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

