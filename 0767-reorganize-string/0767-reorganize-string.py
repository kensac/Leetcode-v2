class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, char) for (char, count) in Counter(s).items()]
        heapify(heap)

        ans = []
        

        while heap:
            print(heap, ans)
            first_count, first_char = heappop(heap)
            if not ans or ans[-1] != first_char:
                ans.append(first_char)
                if first_count + 1 != 0:
                    heappush(heap, (first_count + 1, first_char))
            else:
                if not heap:
                    return ''
                second_count, second_char = heappop(heap)
                ans.append(second_char)
                if second_count + 1 != 0:
                    heappush(heap, (second_count + 1, second_char))
                heappush(heap, (first_count, first_char))
        
        return ''.join(ans)
