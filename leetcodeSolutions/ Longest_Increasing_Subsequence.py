class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        dp = [1]*n
        i=1
        j=0
        while(i<n):
            while(j<i):
                if(nums[j]<nums[i]):
                    dp[i] = max(dp[i],dp[j]+1)
                j+=1
            j=0
            i+=1
        return max(dp)
        