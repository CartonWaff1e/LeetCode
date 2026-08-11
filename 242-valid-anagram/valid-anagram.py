class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lis = sorted(list(s))
        lit = sorted(list(t))
        for i in range(len(lis)):
            if lis[i] != lit[i]:
                return False
        return True
        
        