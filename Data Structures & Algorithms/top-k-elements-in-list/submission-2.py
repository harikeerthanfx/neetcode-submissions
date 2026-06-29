class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for x in nums:
            if x not in hash:
                hash[x] = 1
            else:
                hash[x] += 1
        
        sorted_hash = sorted(hash.items(), key = lambda x:x[1], reverse=True )
        
        print(sorted_hash)

        res = []
        i = 0
        for key, value in sorted_hash:
            if i<k:
                res.append(key)
                i+=1
            else:
                return res
        return res
            
        