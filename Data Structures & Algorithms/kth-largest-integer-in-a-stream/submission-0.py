class KthLargest:
    # IN: stream of values including duplicates
    # OUT: kth largest integer in the stream
    # EDGES: 0 length stream, repeat values
    # CONSTRAINTS: 
    # [1,1000] k
    # [0,1000] len stream
    # [-1000,1000] values
    # Always k integers in stream searching for kth integer

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # what if we have less than k values?
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
