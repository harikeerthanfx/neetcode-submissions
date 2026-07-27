class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dates = [] #temp,index

        for i, t in enumerate (temperatures):
            while dates and t > dates[-1][0] :
                    print("this is the while looop")
                    temp , index = dates.pop()
                    temperatures[index] = i - index
            dates.append([t,i])
        
        while dates:
                temp , index = dates.pop()
                temperatures[index] = 0
        
        return temperatures