class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1 = m - 1
        ptr_2 = len(nums2) - 1
        insert = len(nums1) - 1
        while ptr_1 >= 0 and ptr_2 >= 0:
            if nums2[ptr_2] > nums1[ptr_1]:
                nums1[insert] = nums2[ptr_2]
                ptr_2 -= 1
            else:
                nums1[insert] = nums1[ptr_1]
                ptr_1 -= 1

            insert -= 1
        
        while ptr_2 >= 0:
            nums1[insert] = nums2[ptr_2]
            ptr_2 -= 1
            insert -=1
