class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n<1:
            return 0
        buy = -prices[0]
        sell = 0
        
        for i in range(1, n):
            # either dont buy today and keep last buy as buy or buy the stock on current price based on last sell
            buy = max(buy, sell-prices[i])
            # dont sell and hold or sell based on previous bought price
            sell = max(sell, buy+prices[i]-fee)
            
        # maximum profit must be in sell state
        return sell
        