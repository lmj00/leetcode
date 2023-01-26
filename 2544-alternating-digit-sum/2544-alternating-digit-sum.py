class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        result = 0
        n = str(n)
        
        for i in range(0, len(n) - 1, 2):
            result += int(n[i]) - int(n[i + 1])
        
        if len(n) % 2 != 0:
            result += int(n[-1])

        return result