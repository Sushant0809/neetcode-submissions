class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        

        ans = {}


        for i,num in enumerate(nums):

            diff = target-num
            print(ans)
            print(diff)

            if diff in ans:
                return [ans[diff],i]
            else:
                ans[num] = i
        
        return []