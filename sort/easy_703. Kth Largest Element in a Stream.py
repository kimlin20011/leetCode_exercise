class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # 建立k個數的heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:  # 不滿k個數，直接push
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)  # 放入新元素並取出最小元素
        return self.heap[0]  # 回傳最小數

        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)

        # 使用minHeap => priority queue實作
