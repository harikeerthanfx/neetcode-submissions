class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            target = -nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums) - 1
            
            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                
                if nums[j] + nums[k] == target:
                    print(f"i , j , k = {i}, {j}, {k}")
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            
        return res