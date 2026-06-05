class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        if strs == []: return "*"
        for i in range(len(strs)):
            if i < len(strs) - 1:
                res += strs[i] + '~'
            else:
                res += strs[i]
        
        return res

    def decode(self, s: str) -> List[str]:
        if s == "*": return []
        return s.split('~')