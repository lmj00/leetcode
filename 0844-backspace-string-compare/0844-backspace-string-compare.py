class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        ss = []
        tt = []        
        
        for i in s:
            if i == '#':
                if len(ss) >= 1:
                    del ss[-1]
            else:
                ss.append(i)
        
        
        for j in t:
            if j == '#':
                if len(tt) >= 1:
                    del tt[-1]
            else:
                tt.append(j)
                
        
        return ss == tt