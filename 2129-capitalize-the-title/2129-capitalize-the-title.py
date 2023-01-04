class Solution:
    def capitalizeTitle(self, title: str) -> str:

        t = title.lower().split()
        s = ''
        
        for i in t:
            if len(i) > 2:
                s += i[0].upper() + i[1:]
            else:
                s += i
                
            s += ' '
            
        return s.rstrip()