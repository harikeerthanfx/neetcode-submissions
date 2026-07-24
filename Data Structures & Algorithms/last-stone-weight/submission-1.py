class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        for i in range(len(maxheap)):
            maxheap[i] = -maxheap[i]
        heapq.heapify(maxheap)
        print(maxheap)

        while len(maxheap) > 1:
            #always negate
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            print(f"here is the maxheap = {maxheap}")
            if x == y:
                continue
            else:
                heapq.heappush(maxheap, -abs(x-y))
                print(maxheap)
        
        if maxheap:
            return -maxheap[0]
        else:
            return 0