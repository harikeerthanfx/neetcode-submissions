class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ""
        for ch in s:
            if ch.isalnum():
                arr += ch.lower()
        
        print(arr)
        i = 0
        j = len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:
                return False
            print(f"check i,j = {i}, {j}")
            i += 1
            j -= 1

        return True