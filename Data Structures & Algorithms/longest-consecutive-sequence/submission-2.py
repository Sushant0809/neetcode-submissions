class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash = set(nums)

        maxi = 0
        for n in hash:
            if n-1 not in hash:
                curr = n
                k = 0

                while curr in hash:
                    k+=1
                    curr+=1
                
                maxi = max(k,maxi)
        
        return maxi
        