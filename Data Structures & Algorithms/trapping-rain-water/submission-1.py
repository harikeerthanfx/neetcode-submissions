class Solution:
    def fll(self,height: List[int],idx:int):
        i = idx
        largest = height[idx]
        flag = 0
        while i>0:
            i=i-1
            if height[i] >= largest:
                flag = 1
                largest = height[i]
        if flag == 0:
            return 0
        return largest

    def frl(self,height:List[int],idx:int):
        i = idx
        largest = height[idx]
        flag = 0
        while i<(len(height)-1):
            i += 1
            if height[i] >= largest:
                flag = 1
                largest = height[i]
        if flag == 0:
            return 0
        return largest

    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            if self.fll(height,i)!=0 and self.frl(height,i)!=0:
                print(f"i = {i}\n leftlargest = {self.fll(height,i)} \n rightlargest = {self.frl(height,i)} \n height[i] = {height[i]}")
                water = min ( self.fll(height,i) , self.frl(height,i) ) - height[i]
                area = area + water
            else:
                print(f"i = {i} \n pass")
        return area
