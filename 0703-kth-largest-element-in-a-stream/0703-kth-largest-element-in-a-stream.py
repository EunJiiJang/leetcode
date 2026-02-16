class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num = k
        self.lst = nums

    def add(self, val: int) -> int:
        self.lst.append(val)
        self.lst.sort(reverse=True)
        return self.lst[self.num-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)