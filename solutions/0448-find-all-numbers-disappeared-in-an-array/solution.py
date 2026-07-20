class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            correct_idx=nums[i]-1

            if nums[i]!=nums[correct_idx]:
                nums[correct_idx],nums[i]=nums[i],nums[correct_idx]
            else:
                i+=1
            
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
