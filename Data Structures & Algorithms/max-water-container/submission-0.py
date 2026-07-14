class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        areaMax = 0

        while low < high:
            area = (high - low) * min(heights[low], heights[high])
            areaMax = max(areaMax, area)

            if heights[low] < heights[high]:
                low += 1
            elif heights[low] > heights[high]:
                high -= 1
            else:
                if heights[low+1] > heights[high-1]:
                    low += 1
                else:
                    high -= 1
        
        return areaMax
        