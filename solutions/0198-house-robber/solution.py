class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0

        for num in nums:
            new_total=max(prev1,prev2+num)

            prev2=prev1
            prev1=new_total
        
        return prev1
