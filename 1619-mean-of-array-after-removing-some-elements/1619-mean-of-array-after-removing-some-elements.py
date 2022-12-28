class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        
        arr.sort()
        
        v = round(len(arr) * 0.05)

        rm_arr = arr[v:len(arr) - v]

        return sum(rm_arr) / len(rm_arr)