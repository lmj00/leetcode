class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr) - 2):
            count = 0
            
            for j in range(i, i + 3):
                if arr[j] % 2 == 0:
                    break
                else:
                    count += 1
                    
            if count == 3:
                return True
