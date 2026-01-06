class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bisect left gives us insert position
        # use natural sorting property of bisect function
        subsequence = []

        for num in nums:
            i = bisect_left(subsequence, num)

            if i == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[i] = num
            
        return len(subsequence)