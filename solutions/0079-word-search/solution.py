class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c,index):
            # 1. Base case: we found all letters
            if index==len(word):
                return True

            # 2. Boundary and match check          
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[index]):
                return False

            # 3. Mark as visited (use a dummy value)
            temp=board[r][c]
            board[r][c]='#' 

            # 4. Check all 4 directions
            found= (dfs(r+1,c,index+1)or
                    dfs(r-1,c,index+1)or
                    dfs(r,c+1,index+1)or
                    dfs(r,c-1,index+1))

            # 5. Backtrack (unmark)
            board[r][c]=temp
            return found

        # Start searching from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

        
