class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all=0
        for num in nums:
            xor_all^=num
        
        # xor_all has xor of those two unique numbers and they differ in atleast one bit we find that bit and put it in diff_bit
        diff_bit=xor_all & -xor_all
    
        num1=0
        num2=0
        for num in nums:
            # Now numbers with the bit on at that position go here and doublets cancel out leaving only that one
            if num & diff_bit:
                num1^=num
            # And number with bit off at that position go here and doublets cancel out leaving only that one
            else:
                num2^=num
        
        return [num1,num2]
