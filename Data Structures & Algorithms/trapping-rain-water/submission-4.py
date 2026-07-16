class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for i in range(len(height))]
        maxRight = [0 for i in range(len(height))]
        minLR = [0 for i in range(len(height))]

        maxL = height[0]
        maxR = height[len(height)-1]

        for i in range(1, len(height)):
            maxLeft[i] = maxL
            maxL = max(maxL, height[i])

        for i in range(len(height)-2, -1, -1):
            maxRight[i] = maxR
            maxR = max(maxR, height[i])

        trapped = 0
        for i in range(len(height)):
            minLR[i] = min(maxLeft[i], maxRight[i])
            trapped += max(0, minLR[i] - height[i])
        
        return trapped