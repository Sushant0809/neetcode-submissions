class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {'}':'{',']':'[',')':'('}

        st = []

        for c in s:
            if c in mapping:
                if st and mapping[c]==st[-1]:
                    st.pop()
                else:
                    return False
            
            else:
                st.append(c)
        
        return True if not st else False
