class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        count = 0
        n = list(str(n))
        
        for i in range(len(n) - 1, -1, -1):
            
            if count == 3:
                n.insert(i + 1, '.')
                count = 0
                
            count += 1
        
        return ''.join(n)