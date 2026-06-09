class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s1 = ""
        for c in s:
            if 'A'<=c<='Z':
                c = chr(ord(c) + 32)
            
            if 'a'<=c<='z' or '0'<=c<='9':
                s1+=c
        
        if s1==s1[::-1]:
            return True
        else:
            return False

