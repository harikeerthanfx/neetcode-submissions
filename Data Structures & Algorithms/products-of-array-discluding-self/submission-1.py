class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prod = 1
        for x in nums:
            prod = prod * x
            prefix.append(prod)

        postfix = []
        prod = 1
        for x in reversed(nums):
            prod = prod * x
            postfix.append(prod)
        postfix = list(reversed(postfix))

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(postfix[i+1] * prefix[i-1])
        
        return res
                

        