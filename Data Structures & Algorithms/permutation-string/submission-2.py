class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str_1_sorted = "".join(sorted(s1))
        
        l = len(s1)
        left = 0
        while left < len(s2):
            if s2[left] in s1:
                new_str = s2[left:left+l]
                new_str_sorted = "".join(sorted(new_str))
                if new_str_sorted == str_1_sorted:
                    print(f"current string:{new_str}")
                    return True
            left+=1
        return False