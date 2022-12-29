from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        ls = [j for i in edges for j in i]
        
        return Counter(ls).most_common()[0][0]        