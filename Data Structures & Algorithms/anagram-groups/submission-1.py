from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ang = defaultdict(list)

        for word in strs:
            word1 = ''.join(sorted(word))
            ang[word1].append(word)
        
        return list(ang.values())
        

            
        