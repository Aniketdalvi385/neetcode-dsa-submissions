class Solution:

    # Brute Force and Not a real solution
    # def encode(self, strs: List[str]) -> str:
    #     res = ''
    #     if strs == []: return "*"
    #     for i in range(len(strs)):
    #         if i < len(strs) - 1:
    #             res += strs[i] + '~'
    #         else:
    #             res += strs[i]
        
    #     return res

    # def decode(self, s: str) -> List[str]:
    #     if s == "*": return []
    #     return s.split('~')

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#': j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length

        return res