from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        for i in Counter(arr).most_common():
            if i[0] == i[1]:
                return i[0]
        
        return -1