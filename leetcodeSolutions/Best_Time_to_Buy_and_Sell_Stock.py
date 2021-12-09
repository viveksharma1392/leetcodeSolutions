class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_max = 0
        n = len(prices)
        # rightArray to find maximum element on right of an element
        rightArray = [0]*n
        i = n
        for x in reversed(prices):
            i-=1
            if i==(n-1):
                rightArray[i] = 0
                right_max = x
                continue
            rightArray[i] = right_max
            right_max = max(x, right_max)
        sol=0
        i=0
        for x in prices:
            sol = max(sol, rightArray[i]-x)
            i+=1
        return sol