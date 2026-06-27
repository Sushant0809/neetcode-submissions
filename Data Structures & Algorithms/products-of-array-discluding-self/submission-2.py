class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        ans = [1]*len(nums)

        for i,n in enumerate(nums):
            ans[i]=prefix
            prefix*=n
        
        
        postfix = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        
        return ans
        