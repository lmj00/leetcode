class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        st = sentence.split()
        
        v = st[0][-1]
        
        for i in range(1, len(st)):
            if v != st[i][0]:
                return False
            
            v = st[i][-1]
        
        if st[0][0] == v:
            return True
        
        return False