class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(candidates, target, idx, cur_sum, cur_nums):
            if cur_sum > target:
                return

            if cur_sum == target:
                result.append(cur_nums.copy())
                return

            for i in range(idx, len(candidates)):
                backtrack(
                    candidates,
                    target,
                    i,
                    cur_sum + candidates[i],
                    cur_nums + [candidates[i]],
                )
        
        backtrack(candidates, target, 0, 0, [])
        return result