class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numbs = sorted(set(nums))
        if len(numbs) < 3:
            return max(numbs)
        return numbs[-3]

        # m1 = m2 = m3 = None
        
        # for n in nums:
        #     # Skip if we have already seen this number
        #     if n == m1 or n == m2 or n == m3:
        #         continue
            
        #     # Update the three maximums
        #     if m1 is None or n > m1:
        #         m3, m2, m1 = m2, m1, n
        #     elif m2 is None or n > m2:
        #         m3, m2 = m2, n
        #     elif m3 is None or n > m3:
        #         m3 = n
        
        # # Return m3 if it exists, otherwise return the largest (m1)
        # return m1 if m3 is None else m3

