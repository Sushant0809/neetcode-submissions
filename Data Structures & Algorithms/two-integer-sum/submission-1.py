class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        res = []

        for i,num in enumerate(nums):
            if target-num in hash:
                return [hash[target-num],i]
            
            hash[num] = i

        return []      
        