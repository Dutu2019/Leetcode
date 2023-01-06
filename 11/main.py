class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0
        maxArea = 0

        while right != left:
            maxArea = max(maxArea, min(height[right], height[left]) * (right - left))
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea




solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))