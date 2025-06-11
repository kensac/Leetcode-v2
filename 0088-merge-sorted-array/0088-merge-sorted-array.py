class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1

        # Essentially combine 1 and 2 and split 3 into 2 parts
        # 1 Check if nums1[m] > nums2[n]
        # 2 if m goes below 0
            # keep working with numbers from nums2
        # 3 if n goes below 0
            # then the rest of the array is nums1 so we can stop

        for i in range(len(nums1) - 1, -1, -1):
            if n < 0:
                break
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
