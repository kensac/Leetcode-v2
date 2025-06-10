class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # gain = [-2, -2, -2, +3, +3]

        if sum(gas) < sum(cost):
            return -1

        cur_tank = 0
        res = 0

        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]

            if cur_tank < 0:
                cur_tank = 0
                res = i + 1
        return res
