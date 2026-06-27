class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        freq_s1 = {}
        freq = {}

        for c in s1:
            freq_s1[c] = freq_s1.get(c,0)+1
        
        left = 0

        for right in range(len(s2)):
            freq[s2[right]] = freq.get(s2[right],0)+1

            if right>=len(s1):
                freq[s2[right-len(s1)]]-=1
                if freq[s2[right-len(s1)]]==0:
                    freq.pop(s2[right-len(s1)])
            
            if freq == freq_s1:
                return True
        
        return False


        