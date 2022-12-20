class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        ls = []
        i = 1
        
        while True:
            if len(ls) == k:
                return ls[-1]                
            
            if i not in arr:
                ls.append(i)
                
            i += 1
            