class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkAnagram(s: str, t: str) -> bool:
            if len(s) != len(t): return False
            seen = dict()
            for ch in s:
                seen[ch] = seen.get(ch, 0) + 1

            for ch in t:
                if ch not in seen or seen[ch] == 0:
                    return False
                seen[ch] -= 1
            
            return True

        res = []
        for i in strs:
            isValid = False
            for j in res:
                isValid = checkAnagram(i , j[0])
                if isValid:
                    j.append(i)
                    break
            if not isValid:
                res.append([i])

        return res