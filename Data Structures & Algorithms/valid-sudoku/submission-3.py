class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.': continue
                
                boxid = (i//3, j//3)
                if (curr in rows[i] or curr in cols[j] or curr in boxes[boxid]): 
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                boxes[boxid].add(curr)

        return True