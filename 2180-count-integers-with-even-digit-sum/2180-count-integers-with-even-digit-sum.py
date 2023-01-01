class Solution:
    def countEven(self, num: int) -> int:
            
        count = 0
        for i in range(1, num + 1):
            result = 0
            
            for j in str(i):
                result += int(j)
            
            if result % 2 == 0:
                count += 1

        return count