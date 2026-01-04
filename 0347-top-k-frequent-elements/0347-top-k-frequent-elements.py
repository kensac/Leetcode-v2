class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in counter.items():
            buckets[value].append(key)

        result = []
        i = len(buckets) - 1
        while k > 0:
            if buckets[i]:
                result.append(buckets[i].pop())
                k -= 1
            else:
                i -= 1

        return result
