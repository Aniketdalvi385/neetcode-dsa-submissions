class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        # Full brute force solution just not optimal because of the complexity of coding it
        # A single sign mismatch between -/+ can break whole validation
        # for i in range(9):
        #     for j in range(9):
        #         curr = board[i][j]
        #         if curr != '.':
        #             for k in range(9):
        #                 if k != i and curr != '.' and curr == board[k][j]:
        #                     return False
        #             for k in range(9):
        #                 if k != j and curr != '.' and curr == board[i][k]:
        #                     return False
        #             if (i+1)%3 == 1 and (j+1)%3 == 1:
        #                 if board[i+1][j+1] == curr or board[i+1][j+2] == curr or board[i+2][j+1] == curr or board[i+2][j+2] == curr:
        #                     return False
        #             elif (i+1)%3 == 1 and (j+1)%3 == 2:
        #                 if board[i+1][j-1] == curr or board[i+2][j-1] == curr or board[i+1][j+1] == curr or board[i+2][j+1] == curr:
        #                     return False
        #             elif (i+1)%3 == 1 and (j+1)%3 == 0:
        #                 if board[i+1][j-1] == curr or board[i+2][j-1] == curr or board[i+1][j-2] == curr or board[i+2][j-2] == curr:
        #                     return False
        #             elif (i+1)%3 == 2 and (j+1)%3 == 1:
        #                 if board[i-1][j+1] == curr or board[i-1][j+2] == curr or board[i+1][j+1] == curr or board[i+1][j+2] == curr:
        #                     return False
        #             elif (i+1)%3 == 2 and (j+1)%3 == 2:
        #                 if board[i-1][j-1] == curr or board[i-1][j+1] == curr or board[i+1][j-1] == curr or board[i+1][j+1] == curr:
        #                     return False
        #             elif (i+1)%3 == 2 and (j+1)%3 == 0:
        #                 if board[i-1][j-1] == curr or board[i-1][j-2] == curr or board[i+1][j-1] == curr or board[i+1][j-2] == curr:
        #                     return False
        #             elif (i+1)%3 == 0 and (j+1)%3 == 1:
        #                 if board[i-1][j+1] == curr or board[i-2][j+1] == curr or board[i-1][j+2] == curr or board[i-2][j+2] == curr:
        #                     return False
        #             elif (i+1)%3 == 0 and (j+1)%3 == 2:
        #                 if board[i-1][j-1] == curr or board[i-2][j-1] == curr or board[i-1][j+1] == curr or board[i-2][j+1] == curr:
        #                     return False
        #             elif (i+1)%3 == 0 and (j+1)%3 == 0:
        #                 if board[i-1][j-1] == curr or board[i-2][j-1] == curr or board[i-1][j-2] == curr or board[i-2][j-2] == curr:
        #                     return False
        # return True

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
