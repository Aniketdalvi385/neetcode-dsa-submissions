class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force Solution
        # map = {}
        # res = []
        # for i in nums:
        #     map[i] = map.get(i, 0) + 1
        #     if len(res) < k and i not in res:
        #         res.append(i)
        #     elif i not in res:
        #         for ind, j in enumerate(res):
        #             if map[j] < map[i]:
        #                 res[ind] = i
        #                 break
        # return res

        map = {}
        res = []
        for i in nums:
            map[i] = map.get(i, 0) + 1
            if i not in res: 
                if len(res) < k:
                    res.append(i)
                else:
                    for ind, j in enumerate(res):
                        if map[j] < map[i]:
                            res[ind] = i
                            break
        return res