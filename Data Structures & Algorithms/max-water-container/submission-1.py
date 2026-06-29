class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        maximum = 0
        while left < right:
            dist = abs(left - right)
            ht = min(heights[left],heights[right])
            product = dist * ht

            if product > maximum:
                maximum = product

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maximum