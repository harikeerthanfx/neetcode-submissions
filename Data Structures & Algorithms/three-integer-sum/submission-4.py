class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print (nums)
        res = []
        for i in range(len(nums)):
            j , k = 0 ,  len(nums)-1
            target = -nums[i]
            while j<i and k>i:
                if nums[j]+nums[k]<target:
                    j+=1
                elif nums[j]+nums[k]>target:
                    k-=1
                elif nums[j]==0 and nums[k]==0 and target==0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
        return res
                


