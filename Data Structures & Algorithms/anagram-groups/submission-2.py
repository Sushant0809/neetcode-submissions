from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ang = defaultdict(list)

        for word in strs:
            w = [0]*26
            for c in word:
                w[ord(c)-ord('a')]+=1
            ang[tuple(w)].append(word)
        
        return list(ang.values())
        

            
        