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
            # Largest value
            x = heapq.heappop_max(stones)
            # Second largest value
            y = heapq.heappop_max(stones) 

            x -= y
            y -= y

            if x > 0:
                heapq.heappush_max(stones, x)
            
        return 0 if len(stones) < 1 else stones[0]