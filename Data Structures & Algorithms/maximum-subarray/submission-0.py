class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        

        total = nums[0]
        prefix = nums[0]

        for num in nums[1:]:  
            if prefix<0:
                prefix = 0
            prefix+=num
            print(prefix)
            total = max(total, prefix)
            
        
        return total
        