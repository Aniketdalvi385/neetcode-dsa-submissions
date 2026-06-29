class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force solution with time complexity: O(n*m log m) space: O(1)
        # key = "".join(sorted(s1))
        # pt1, pt2 = 0, 0
        # while pt2 < len(s2):
        #     while (pt2-pt1)+1 < len(s1):
        #        pt2 += 1
        #     if (pt2-pt1)+1 == len(s1):
        #         curr = "".join(sorted(s2[pt1:pt2+1]))
        #         if curr == key:
        #             return True
        #         pt1 += 1
        
        # return False

        # Optimal Solution
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        s1_count = [0]*26
        s2_count = [0]*26

        for i in range(n1):
            s1_count[ord(s1[i]) - 97] += 1
            s2_count[ord(s2[i]) - 97] += 1

        if s1_count == s2_count: return True

        for i in range(n1, n2):
            s2_count[ord(s2[i]) - 97] += 1
            s2_count[ord(s2[i-n1]) - 97] -= 1
            if s1_count == s2_count: return True

        return False