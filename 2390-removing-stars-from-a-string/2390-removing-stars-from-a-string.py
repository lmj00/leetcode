class Solution:
    def removeStars(self, s: str) -> str:
        
        ss = []
        
        for i in s:
            if i == '*':
                del ss[-1]
            else:
                ss.append(i)

        return ''.join(ss)