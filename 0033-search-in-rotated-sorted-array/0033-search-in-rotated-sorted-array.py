class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        def binary(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # find which half we want to search
        print(right)
        if nums[right] <= target <= nums[-1]:
            return binary(nums, target, right, len(nums) - 1)
        # right + 1
        else:
            return binary(nums, target, 0, right - 1)
        
