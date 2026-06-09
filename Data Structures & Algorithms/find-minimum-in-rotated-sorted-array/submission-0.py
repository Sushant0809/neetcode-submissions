class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mini = 0
        for j in range(len(nums)-1,-1,-1):

            if nums[j]>nums[j-1]:
                continue
            else:
                break
        
        return nums[j]
