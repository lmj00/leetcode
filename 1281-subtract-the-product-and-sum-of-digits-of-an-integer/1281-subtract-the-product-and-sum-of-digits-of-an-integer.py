from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n = list(map(int, str(n)))

        s = sum(n)
        m = reduce(lambda x, y: x * y, n)
        
        return m - s    