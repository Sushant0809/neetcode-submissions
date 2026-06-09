class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0]*26

        if len(s)!=len(t):
            return False

        for c in s:
            freq[ord(c) - ord('a')] +=1
        
        for c in t:
            ind = ord(c)-ord('a')
            freq[ind] -=1
            if freq[ind]<0:
                return False
        
        return True