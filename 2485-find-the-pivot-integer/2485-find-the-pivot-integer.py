class Solution:
    def pivotInteger(self, n: int) -> int:
        
        ls = [i for i in range(1, n + 1)]
        
        
        for i in range(n):
            left = sum(ls[:i + 1]) 
            right = sum(ls[i:])
                
            if left == right:
                return i + 1
            
        return -1