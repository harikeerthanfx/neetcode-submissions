class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = {}

        for i in range(len(position)):
            car[position[i]] = speed[i]
        
        car = dict(sorted(car.items()))

        fleet = 0
        stack = []
        for key, value in reversed(car.items()):
            time = (target - key)/value

            if stack and time > stack[-1]:
                stack.pop()
                stack.append(time)
                fleet += 1
            elif stack and time <= stack[-1]:
                continue
            else:
                fleet += 1
                stack.append(time)

        return fleet

