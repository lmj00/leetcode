class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        ls = [(names[i], heights[i]) for i in range(len(names))]
         
        val = sorted(ls, key=lambda x:x[1], reverse=True)
        
        result = [i[0] for i in val]
        
        return result
