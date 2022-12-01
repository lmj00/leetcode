class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        [nums1.remove(nums1[i]) for i in range(len(nums1) - 1, m -1, -1)]

        nums1 += [i for i in nums2]            
        
        nums1.sort() 