class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        held = -float("inf")
        sold = 0
        reset = 0

        for price in prices:
            prev_held = held
            prev_sold = sold
            prev_reset = reset

            held = max(prev_held, prev_reset - price)
            sold = prev_held + price
            reset = max(prev_reset, prev_sold)

        return max(sold, reset)

