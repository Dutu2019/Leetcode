from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        right = left = 0
        res = 0

        for right, r in enumerate(s):
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        print(res)
    


Solution.lengthOfLongestSubstring("pwwkew")
        