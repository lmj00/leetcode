class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        num = str(num)
        count = 0
        
        for i in range(len(num) - k + 1):
            v = int(num[i: i + k])
            
            if v != 0 and int(num) % v == 0:
                count += 1
        
        return count