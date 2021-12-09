class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        
        # Consider a dp 2D array where rows = length od String +1 and columns = length of pattern +1
        # Add extra row and column in dp and set dp[0][0] True as if string and pattern are blank we should return True

        # for first row which indicates blank string where pattern like a*b* should be True check zero occurance condition
        # for every * 
            # case 1 - consider 0 occurance of char before * so dp[i][j] = dp[i][j-2]

        # for every . or char match set dp[i][j] = dp[i-1][j-1]
        # for every * 
            # case 1 - consider 0 occurance of char before * so dp[i][j] = dp[i][j-2]
            # case 2 - Consider 1 or more occuance of char check if ( s[i-1]==p[j-2] or p[j-2]=="." ) if yes set dp[i][j]=dp[i-1][j]

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

    