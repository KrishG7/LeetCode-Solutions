class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        # def backtrack(start,path):
        #     if len(path)==k :
        #         res.append(list(path))
        #         return

        #     for i in range(start,n+1):
        #             path.append(i)
        #             backtrack(i+1,path)               
        #             path.pop()
        
        # backtrack(1,[])
        # return res

# Pruned version:
        def backtrack(start, path):
            if len(path) == k:
                res.append(list(path))
                return
            
            # Optimization: Only loop until (n - (k - len(path)) + 1)
            # This prevents the loop from running when it's impossible to form a full combination
            remaining_needed = k - len(path)
            for i in range(start, n - remaining_needed + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1,[])
        return res
