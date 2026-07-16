class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        leftMax = height[left]
        rightMax = height[right]
        trapped = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                trapped += max(0, leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                trapped += max(0, rightMax - height[right])
        
        return trapped