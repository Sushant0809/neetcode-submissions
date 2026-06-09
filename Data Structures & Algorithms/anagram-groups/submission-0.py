class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = {}

        for s in strs:

            s1 = ''.join(sorted(s))

            if s1 in hash:
                hash[s1].append(s)
            else:
                hash[s1] = [s]
        
        ans = []

        for b in hash.values():
            ans.append(b)

        return ans


