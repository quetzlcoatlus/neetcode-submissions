class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap
        # See the top two values
        # Keep track of index of second value
        # Do collision
        # Remove the elements that are now 0
        # Continue until len < 2
        # Heapify again
        # Return last value or 0 if empty

        import heapq
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # Difference of two largest values
            cur = heapq.heappop_max(stones) - heapq.heappop_max(stones)

            if cur > 0:
                heapq.heappush_max(stones, cur)
            
        return 0 if len(stones) == 0 else stones[0]