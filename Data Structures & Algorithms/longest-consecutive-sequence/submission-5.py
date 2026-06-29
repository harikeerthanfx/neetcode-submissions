class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        required = []
        required.append(nums[0])
        max = 1
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                if count>max:
                    max=count
                continue
            elif nums[i]!=nums[i-1]+1:
                required = []
                required.append(nums[i])
                count = 1
            elif nums[i] == nums[i-1]+1:
                required.append(nums[i])
                count+=1

            if count>max:
                max = count

        return max