class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1

        for num in nums[1:]:
            if num == res:
                count += 1
            else:
                count -=1
            if count < 0:
                count = 0
                res = num
        return res