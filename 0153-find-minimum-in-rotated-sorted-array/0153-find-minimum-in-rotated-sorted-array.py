class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            print(mid, nums[left], nums[mid], nums[right])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        # 2,3,4