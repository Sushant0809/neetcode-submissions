class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == '.':
                    continue
                
                k = board[r][c]
                if k in rows[r] or k in cols[c] or k in sqrs[(r//3,c//3)]:
                    return False
                
                rows[r].add(k)
                cols[c].add(k)
                sqrs[(r//3,c//3)].add(k)
        
        return True
        