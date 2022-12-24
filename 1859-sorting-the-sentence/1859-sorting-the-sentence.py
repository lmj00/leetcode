import re

class Solution:
    def sortSentence(self, s: str) -> str:
         
        s = sorted(s.split(), key=lambda x:x[-1])
        v = ''
        
        for i in range(len(s)):
            v += s[i].replace(s[i][-1], ' ') 
        
        return v.rstrip()