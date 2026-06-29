class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            if target-x in nums:
                j = nums.index(target-x)
                if i != j:
                    return sorted([i,j])
        return []
