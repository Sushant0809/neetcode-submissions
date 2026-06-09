class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash = {}

        for num in nums:
            hash[num] = 1
        
        maxi = 0
        for num in hash:

            if num-1 not in hash:
                curr = num
                k=0

                while curr in hash:
                    k+=1
                    curr+=1
            
                maxi = max(maxi,k)

        return maxi


        

        