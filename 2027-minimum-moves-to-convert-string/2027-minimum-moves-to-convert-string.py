class Solution:
    def minimumMoves(self, s: str) -> int:
        
        result = 0
        i = 0
        
        while i < len(s):
            if s[i] != 'O' and 'X' in s[i:i + 3]:
                result += 1
                i += 3
            else:
                i += 1

            
        return result