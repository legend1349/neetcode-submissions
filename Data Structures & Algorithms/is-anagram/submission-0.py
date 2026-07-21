class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic_s = {}
        dic_t = {}
    
        for l in s:
            if l in dic_s:
                dic_s[l] += 1
            else:
                dic_s[l] = 1

        for l in t:
            if l in dic_t:
                dic_t[l] += 1
            else:
                dic_t[l] = 1

        return dic_s == dic_t