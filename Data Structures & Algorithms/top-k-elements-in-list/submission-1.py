class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        req_list=[]
        for i in nums:
            if i in groups:
                groups[i]=groups[i] + 1
            else:
                groups[i]=1
        
        sorted_items=sorted(groups.items(),key=lambda x:x[1], reverse=True)
        key_list=[key for key,value in sorted_items]

        for i in range(k):
            req_list.append(key_list[i])
        
        return req_list
        
            
