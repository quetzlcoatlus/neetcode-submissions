class KthLargest:
    # IN: stream of values including duplicates
    # OUT: kth largest integer in the stream
    # EDGES: 0 length stream, repeat values
    # CONSTRAINTS: 
    # [1,1000] k
    # [0,1000] len stream
    # [-1000,1000] values
    # Always k integers in stream searching for kth integer

    # Can use a size k minheap
    # k size minheap puts the kth largest value at the top for O(1) retrieval
    # Initialize by heapify and then pop until there's only k elements left
    # Adding we push the value and heapify
    # - Not guaranteed the initialization stream is length k
    # - So check that the length is > k, if it is then pop off the top
    # Just return the top value for the kth largest value

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
