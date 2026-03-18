class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            # 1. 새로 들어온 문자 빈도 업데이트
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. 현재 윈도우에서 가장 많은 문자 수 추적
            max_freq = max(max_freq, count[s[right]])
            
            # 3. 유효하지 않으면 왼쪽을 한 칸 줄임
            window_size = right - left + 1
            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # 4. 현재 유효한 윈도우 크기가 곧 정답 후보
            ans = max(ans, right - left + 1)

        return ans