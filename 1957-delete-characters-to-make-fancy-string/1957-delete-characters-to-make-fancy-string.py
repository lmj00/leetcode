class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s) < 3:
            return s
        
        ss = s[0] + s[1]
        
        for i in range(2, len(s)):
            if ss[-1] == ss[-2] == s[i]:
                continue
                    
            ss += s[i]

        
        return ss