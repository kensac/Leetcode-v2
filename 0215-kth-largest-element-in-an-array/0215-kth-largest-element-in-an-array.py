class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        # Since it is a min heap, we keep popping the smalles elems
        # and then keep the k largest elements
        # klog(k), O(k)
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heappop(heap)
        
        return heap[0]