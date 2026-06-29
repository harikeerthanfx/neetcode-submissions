class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} #value,idx
        for i,x in enumerate(nums):
            if target-x in hash:
                return [hash[target-x],i]
            else:
                hash[x]=i