class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]

        def backtrack(remaining,path,start):
            # Valid Combination found
            if remaining == 0:  
                results.append(list(path))
                return

            #Overshot
            elif remaining<0:
                return

            #Explore candidates
            for i in range(start,len(candidates)):

                #Include candidate in current path
                path.append(candidates[i])

                # Recurse: Pass 'i' again to allow reusing the same element
                backtrack(remaining-candidates[i],path,i)
                
                # Backtrack: Remove candidate to explore other possibilities
                path.pop()
        
        backtrack(target,[],0)
        return results
