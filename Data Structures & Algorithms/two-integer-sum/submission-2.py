class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        liveMap = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in liveMap:
                return [liveMap[diff],i]
            liveMap[n]=i
        return