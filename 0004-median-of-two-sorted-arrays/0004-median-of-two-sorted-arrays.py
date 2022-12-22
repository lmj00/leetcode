class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 += nums2
        nums1.sort()


        v = len(nums1) // 2

        if len(nums1) % 2 == 0:
            return (nums1[v] + nums1[v - 1]) / 2
        
        return nums1[v]