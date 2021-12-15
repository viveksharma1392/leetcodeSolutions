class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0]*(n+1)
        #for currenct tap check its left end coverage and set the left end coverage to max of the tap (right end max)
        for i in range(n+1):
            left = max(0,i-ranges[i]);
            right = min(n,i+ranges[i]);
            dp[left] = max(dp[left],right);
        positionCoverTill = dp[0];
        count = 1;
        currentCover = 0;
        # minimum number of tap required to cover whole garden, 
        for i in range(n+1):
            currentCover = max(currentCover,dp[i]);
            if positionCoverTill<i:
                return -1
            if i==positionCoverTill:
                count+=1;
                positionCoverTill = currentCover;
            
            if positionCoverTill==n:
                return count;
    
        