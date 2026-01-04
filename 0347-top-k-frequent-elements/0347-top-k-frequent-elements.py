class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can also use a heap but only keep top k largest that will make the O(nlogk) which is lesser than nlogn when k < n, however when k == n we can just return everything bringing the time to O(1) and therfore still lower
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
