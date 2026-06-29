class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i,n in enumerate(numbers):
            if target-n in numbers:
                return [i+1,numbers.index(target-n)+1]
