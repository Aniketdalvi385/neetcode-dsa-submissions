class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = "".join(sorted(s1))
        pt1, pt2 = 0, 0
        while pt2 < len(s2):
            while (pt2-pt1)+1 < len(s1):
               pt2 += 1
            if (pt2-pt1)+1 == len(s1):
                curr = "".join(sorted(s2[pt1:pt2+1]))
                print(curr)
                if curr == key:
                    return True
                pt1 += 1
        
        return False