from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n = list(map(int, str(n)))

        s = sum(n)
        m = 1
        
        for i in n:
            m *= i    
        
        return m - s    