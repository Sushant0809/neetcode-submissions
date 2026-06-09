class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        countchr = {}

        l=0
        res = 0

        maxf = 0

        for r in range(len(s)):
            countchr[s[r]] = 1 + countchr.get(s[r],0)
            maxf = max(countchr[s[r]], maxf)

            while (r-l+1) - maxf>k:
                countchr[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res

        
        