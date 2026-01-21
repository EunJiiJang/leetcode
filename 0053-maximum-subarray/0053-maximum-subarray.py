class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        crr = nums[0]
        maxn = nums[0]

        for i in range(1,len(nums)):
            n = nums[i]
            crr = max(n,crr+n)
            maxn = max(maxn,crr)
        return maxn
        