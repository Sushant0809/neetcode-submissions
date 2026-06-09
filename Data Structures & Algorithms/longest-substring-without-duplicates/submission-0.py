class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash = {}

        l = 0 

        res = 0

        for r in range(len(s)):
            while s[r] in hash:
                hash.pop(s[l])
                l+=1
            
            hash[s[r]] = 1
            res = max(res, r-l+1)
        
        return res


        