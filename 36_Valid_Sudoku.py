import collections
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = collections.defaultdict(set)
    subcell_set = collections.defaultdict(set)
    for r in range(9):
        rows = set()
        for c in range(9):
            if board[r][c] == ".":
                continue
            subcell = (r//3)*3 + c//3
            if (board[r][c] in rows) or (board[r][c] in cols[c]) or (board[r][c] in subcell_set[subcell]):
                return False
            rows.add(board[r][c])
            cols[c].add(board[r][c])
            subcell_set[subcell].add(board[r][c])
    return True
