class Solution:
    def removeDuplicates(self, s: str) -> str:
    
        ss = [s[0]]
        
        for i in range(1, len(s)):
            if len(ss) >= 1 and ss[-1] == s[i]:
                del ss[-1]
            else:
                ss.append(s[i])


        return ''.join(ss)