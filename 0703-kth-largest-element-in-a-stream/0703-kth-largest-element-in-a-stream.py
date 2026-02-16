import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num = k
        self.lst = nums
        heapq.heapify(self.lst)
        while len(self.lst) > k:
            heapq.heappop(self.lst)

    def add(self, val: int) -> int:
        heapq.heappush(self.lst,val)
        if len(self.lst) > self.num:
            heapq.heappop(self.lst)
        return self.lst[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)