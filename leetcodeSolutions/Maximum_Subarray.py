class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp = 0
        ans = 0
        for x in nums:
            temp+=x
            ans = max(ans, temp)
            if temp<0:
                temp=0
        if ans==0:
            return max(nums)
        return ans