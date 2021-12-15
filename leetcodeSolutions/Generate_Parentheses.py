class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol = []
        def dfs(left, right, n, curr):
            if left==n and right==n:
                sol.append(curr)
                return
            if right>left or left>n:
                return
            dfs(left+1, right, n, curr+"(")
            dfs(left, right+1, n, curr+")")
            
        dfs(0,0,n,"")
        return sol
        