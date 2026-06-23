class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers=[str(i) for i in range (1,n+1)]
        k=k-1
        res=[]

        fact=math.factorial(n-1)

        for i in range(n-1,0,-1):
            index=k//fact
            res.append(numbers.pop(index))

            k%=fact
            fact//=i
        
        res.append(numbers[0])

        return "".join(res)
        
