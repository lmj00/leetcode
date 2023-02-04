class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        result = 0
        allowed = set(allowed)
        
        for word in words:
            check = 0
            
            for j in word:
                if j in allowed:
                    check += 1
        
            if check == len(word):
                result += 1
                
        return result
    