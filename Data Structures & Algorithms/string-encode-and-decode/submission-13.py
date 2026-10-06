class Solution:

    def encode(self, strs: List[str]) -> str:
        res =''
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#': j+= 1
            l = int(s[i:j])
            curr = s[j+1: j+1+l]
            res.append(curr)
            i = j+1+l
        
        return res