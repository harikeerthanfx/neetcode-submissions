class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        max_area = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                dist = abs(i-j)
                height = min(heights[i],heights[j])
                area = dist * height
                if area > max_area:
                    max_area = area
        return max_area