class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def custom_reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)  # 7
        k %= n
        custom_reverse(0, n - k - 1)
        custom_reverse(n - k, n - 1)
        custom_reverse(0, n - 1)
