class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""

        freq_s,freq_t = {},{}

        left = 0

        for c in t:
            freq_t[c] = freq_t.get(c,0)+1
        
        required = len(freq_t)

        formed = 0

        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            freq_s[s[right]] = freq_s.get(s[right],0)+1
            if s[right] in freq_t and freq_s[s[right]]==freq_t[s[right]]:
                formed+=1
            
            while formed==required:
                if right-left+1<min_len:
                    min_len=right-left+1
                    start = left
                
                freq_s[s[left]]-=1
                if s[left] in freq_t and freq_s[s[left]]<freq_t[s[left]]:
                    formed-=1
                
                if freq_s[s[left]]==0:
                    freq_s.pop(s[left])
                
                left+=1
            
        return s[start:min_len+start] if min_len!=float('inf') else ""





        