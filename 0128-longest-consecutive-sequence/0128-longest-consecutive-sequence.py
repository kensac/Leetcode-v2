class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            cur_longest_sequence = 1
            while num + 1 in nums_set:
                num += 1
                cur_longest_sequence +=1
            longest_sequence = max(cur_longest_sequence, longest_sequence)

        return longest_sequence