class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # Sort the job on the basis of endTime and apply same logic as longest increasing sequence
        # But the only difference is here dp indicated the max profit till now so we cn use break statement
        tuples = []
        n = len(startTime)
        if n ==0:
            return 0
        if n==1:
            return profit[0]
        dp = [0]*n
        for i in range(n):
            t = [startTime[i], endTime[i], profit[i]]
            tuples.append(t)
        tuples.sort(key=lambda x:x[1])
            
        i=1
        dp[0] = tuples[0][2]
        while(i<n):
            j=i-1
            dp[i] = max(dp[i-1],tuples[i][2])
            while(j>-1):
                if tuples[j][1]<=tuples[i][0]:
                    dp[i] = max(dp[i], dp[j]+tuples[i][2])
                    break
                j-=1
            i+=1
        return dp[n-1]
        