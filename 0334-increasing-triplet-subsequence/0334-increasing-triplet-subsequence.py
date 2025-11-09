class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        subsequence = []
        for num in nums:
            i = bisect_left(subsequence, num)
            if i == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[i] = num
            if len(subsequence) >= 3:
                return True

        return False
