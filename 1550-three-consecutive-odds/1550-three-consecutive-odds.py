class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(0, len(arr) - 2):
            s_arr = arr[i:i + 3]
            count = 0
            
            for j in s_arr:
                if j % 2 == 0:
                    break
                else:
                    count += 1
                    
            if count == 3:
                return True
