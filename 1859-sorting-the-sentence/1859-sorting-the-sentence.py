import re

class Solution:
    def sortSentence(self, s: str) -> str:
         
        s = sorted(s.split(), key=lambda x:x[-1])
        
        for i in range(len(s)):
            s[i] = s[i].replace(s[i][-1], '') 

        result = ' '.join(map(str, s))

        return result
