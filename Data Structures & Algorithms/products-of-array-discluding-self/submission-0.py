class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list=[]
        for i in range(len(nums)):
            total=1
            for j in range(len(nums)):
                if j!=i:
                    total=total*nums[j]
            return_list.append(total)
        return return_list
            
