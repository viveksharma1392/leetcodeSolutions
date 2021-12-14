class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1:
            return 0
        
        # dp[i] = max(dp[i-1], prices[i] - prices[j] + dp[j-2]) j = [0, i-1]
        # If we sell the shares on i-th day bought on j-th day, 
        # we couldn't trade on (j-1)-th day because of cooldown. So the last one is dp[j-2].
        
        min_diff = prices[0]
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            min_diff = min(min_diff, prices[i-1]-dp[i-2])
            dp[i] = max(dp[i-1], prices[i-1]-min_diff)
        return dp[-1]