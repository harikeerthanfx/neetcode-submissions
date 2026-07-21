class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []
        lmax = 0
        rmax = 0
        for i in range(len(height)):
            leftmax.append(lmax)
            if height[i] > lmax:
                lmax = height[i]
        for i in range(len(height)-1,-1,-1):
            rightmax.append(rmax)
            if height[i] > rmax:
                rmax = height[i]
        rightmax.reverse()

        print(leftmax)
        print(rightmax)

        count = 0
        for i,ht in enumerate(height):
            addd = min(leftmax[i],rightmax[i]) - ht
            if addd > 0:
                count = count + addd

        return count