class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        sorted_nums = sorted(nums)

        for i,el in enumerate(sorted_nums):
            target = -el

            l = 0
            r = len(sorted_nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                
                if sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] == target:
                    ans = [sorted_nums[l],sorted_nums[i],sorted_nums[r]]
                    if sorted(ans) not in res:
                        res.append(sorted(ans))
                    l += 1
        return res