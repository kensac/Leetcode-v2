class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array in place
        nums.sort()
        res = []

        for i in range(len(nums) - 2): # ensure we don't go over len(nums) w j & k
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target < 0:
                    j += 1
                elif target > 0:
                    k -=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j+=1
                    while k >= 0 and nums[k] == nums[k + 1]:
                        k-=1
        return res

