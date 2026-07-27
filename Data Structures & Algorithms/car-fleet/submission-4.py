class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = {}

        for i in range(len(position)):
            car[position[i]] = speed[i]
        
        car = dict(sorted(car.items()))

        fleet = 0
        lasttime = -1
        for key, value in reversed(car.items()):
            time = (target - key)/value

            if not lasttime == -1 and time > lasttime:
                lasttime = time
                fleet += 1
            elif not lasttime == -1 and time <= lasttime:
                continue
            else:
                fleet += 1
                lasttime = time

        return fleet

