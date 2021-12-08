class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(0,n+1):
            for j in range(1,m+1):
                if i==0:
                    if p[j-1]=="*":
                        dp[i][j]=dp[i][j-2]
                    continue
                elif p[j-1]=="*":
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif p[j-2]==s[i-1] or p[j-2]==".":
                        dp[i][j] = dp[i-1][j]
                elif p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1] 
        return dp[n][m]