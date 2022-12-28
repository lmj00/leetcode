from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
    
        ls = []
        v = sorted(Counter(nums).most_common(), key=lambda x:(x[1], -x[0]))
        
        for i in v:
            for j in range(i[1]):
                ls.append(i[0])
    
    
        return ls