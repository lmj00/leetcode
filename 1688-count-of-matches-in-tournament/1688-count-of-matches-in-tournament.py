class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        result = 0
        
        while n != 1:
            if n % 2 == 0:
                n //= 2
                result += n  
            else:
                n //= 2
                result += n  
                n += 1
            
        return result 