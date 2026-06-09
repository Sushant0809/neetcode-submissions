class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {}

        for c in s1:
            count[c] = 1+count.get(c,0)
        
        l=0

        check = {}

        for r in range(len(s2)):
            check[s2[r]] = 1+check.get(s2[r],0)

            if r-l+1>len(s1):
                check[s2[l]]-=1
                if check[s2[l]] == 0:
                    del check[s2[l]]
                l+=1
            
            if count==check:
                return True
        return False
        