# Lets generalised this problem to Find the maximum profit you can achieve. You may complete at most K transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# i for transaction and j for days - consider 0th ransaction as extra one (means adding a extra row with 0 vlaue in it)
# dp[i][j] = max (case1, case 2)
#   case1 - not doing any transaction dp[i][j-1]
#   case2 - selling the stock which we bought on m-th day profit till now = price[j]-price[m] + dp[i-1][m] where 0<=m<j
#   For case2 we need iteration we want to avoid it - 
#   Consider number of trasaction i= 2  and days j=3 calculate DP[2][3] m will vary from 0,1,2
#   for Case 2 DP[2][3] = max of  DP[1][0]-price[0]+price[3]
#                                 DP[1][1]-price[1]+price[3]
#                                 DP[1][2]-price[2]+price[3]
# price[3] is fix here so we need the max diff for each day 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        n = 3
        dp = [[0]*m for i in range(n)]
        
        for i in range(1,n):
            maxDiff = -prices[0]
            for j in range(1,m):
                maxDiff = max(maxDiff, dp[i-1][j-1]-prices[j-1])
                dp[i][j] = max(dp[i][j-1], maxDiff+prices[j])
        return dp[-1][-1]
    