class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        # If k is very large, this becomes the unlimited transactions problem
        if k >= len(prices) // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))
        
        # buy[j] is the max profit after buying j+1-th stock
        # sell[j] is the max profit after selling j+1-th stock
        buy = [-float('inf')] * k
        sell = [0] * k
        
        for price in prices:
            for j in range(k):
                # Maximize profit of buying: 
                # Either keep previous buy, or sell j-1 and buy current (or just buy if j=0)
                prev_sell = sell[j-1] if j > 0 else 0
                buy[j] = max(buy[j], prev_sell - price)
                
                # Maximize profit of selling:
                # Either keep previous sell, or sell current price after buying j
                sell[j] = max(sell[j], buy[j] + price)
                
        return sell[-1]
