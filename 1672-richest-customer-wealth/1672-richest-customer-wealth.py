class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        v = 0
        
        for i in accounts:
            v = max(v, sum(i))
        
        return v