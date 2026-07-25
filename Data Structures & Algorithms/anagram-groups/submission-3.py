class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for lst in strs:
            if "".join(sorted(lst)) not in group:
                group["".join(sorted(lst))] = [lst]
            else:
                group["".join(sorted(lst))].append(lst)
        
        return list(group.values())

