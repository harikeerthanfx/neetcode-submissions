class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        if n == 1:
            return [0]

        res = [0 for i in range(n)]
        stack = []

        for i in range(n):

            while stack and stack[-1][0]<temperatures[i]:
                elem,index = stack.pop()
                res[index] = i - index
            stack.append([temperatures[i],i])
        return res
