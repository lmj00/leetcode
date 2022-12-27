class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        val = 0
        
        for i in operations:
            if '+' in i:
                val += 1
            else:
                val -= 1
                
        return val 