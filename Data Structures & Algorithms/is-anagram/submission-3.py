class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash = {}

        if len(s)!=len(t):
            return False

        for c in s:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        
        for c in t:
            if c not in hash:
                return False
            else:
                hash[c] -=1
            
            if hash[c]<0:
                return False
        
        return True


        