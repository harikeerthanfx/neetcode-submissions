class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        lmax = [0] * n
        rmax = [0] * n
        
        L = 0
        R = 0
        for i in range(n):
            lmax[i] = L
            L = max(height[i],L)
        
        for i in range(n-1,-1,-1):
            rmax[i] = R
            R = max(R,height[i])
        
        total = 0
        for i,ht in enumerate(height):
            water = min(lmax[i],rmax[i]) - ht
            if water > 0:
                total += water

        return total
