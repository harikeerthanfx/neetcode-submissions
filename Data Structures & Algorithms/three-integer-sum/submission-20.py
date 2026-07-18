class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        sorted_nums = sorted(nums)
        print(sorted_nums)

        for i,el in enumerate(sorted_nums):

            #checking if duplicate element is coming
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            target = -el
            l, r = i+1, len(nums) - 1

            while l < r:
                if sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] == target:
                    print(f" i = {i} l = {l} r = {r}")
                    res.append([sorted_nums[l],sorted_nums[i],sorted_nums[r]])
                    l+=1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l += 1
                    
        return res
