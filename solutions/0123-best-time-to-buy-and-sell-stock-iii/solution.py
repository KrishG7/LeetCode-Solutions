class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        profit1 = 0
        buy2 = float('inf')
        profit2 = 0
        
        for price in prices:
            # 1. Minimize the cost of the first buy
            buy1 = min(buy1, price)
            
            # 2. Maximize the profit of the first sell
            profit1 = max(profit1, price - buy1)
            
            # 3. Minimize the cost of the second buy (using our profit1 as a discount)
            buy2 = min(buy2, price - profit1)
            
            # 4. Maximize the final profit after the second sell
            profit2 = max(profit2, price - buy2)
            
        return profit2
