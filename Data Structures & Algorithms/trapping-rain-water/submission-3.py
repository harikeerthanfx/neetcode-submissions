class Solution:
    def trap(self, height: List[int]) -> int:
        mleft=[]
        mright=[]
        #ht
        water=[]
        
        lmax = 0
        for i in range(len(height)):
            mleft.append(lmax)
            if height[i] > lmax:
                lmax = height[i]

        print(mleft)

        rmax = 0
        for i in range(len(height)-1,-1,-1):
            mright.insert(0,rmax)
            if height[i] > rmax:
                rmax = height[i]
        
        print(mright)

        for i in range(len(height)):
            water.append(min(mleft[i],mright[i]))
            
        print(water)
        print(height)

        tot = 0
        for i in range(len(height)):
            if water[i]-height[i]>0:
                tot += water[i]-height[i]
        
        return tot
        

        