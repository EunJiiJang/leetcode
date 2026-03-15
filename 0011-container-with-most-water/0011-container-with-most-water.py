class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0
        right = len(height)-1
        maxnum = 0
        while left < right:
            maxnum = max(maxnum,(right - left)* min(height[left],height[right])) 
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxnum