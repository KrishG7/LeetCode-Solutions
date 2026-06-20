class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        pos_diag=set()
        neg_diag=set()

        def backtrack(r):
            if r == n:
                return 1

            total_solutions = 0
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
            
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                total_solutions += backtrack(r+1)

                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)

            return total_solutions

        return backtrack(0)
