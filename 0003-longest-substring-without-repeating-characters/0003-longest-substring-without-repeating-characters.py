class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sum = 0
        left = 0
        charSet = set()

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            max_sum=max(max_sum,i-left+1)
        return max_sum