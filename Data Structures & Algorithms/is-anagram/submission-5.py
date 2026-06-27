class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        hash1 = [0]*26
        hash2 = [0]*26

        for c1,c2 in zip(s,t):
            hash1[ord(c1)-ord('a')]+=1
            hash2[ord(c2)-ord('a')]+=1
        
        return hash1==hash2


