class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""

        for st in strs:
            s+=f"{len(st)}#{st}"
        return s

    def decode(self, s: str) -> List[str]:

        result = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=j+1+length
        
        return result
            
        