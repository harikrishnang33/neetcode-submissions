class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        squareSeen = defaultdict(set)

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                num = board[row][col]
                if num == ".":
                    continue

                square = (row//3, col//3)
                
                if num in rowSeen[row] or num in colSeen[col] or num in squareSeen[square]:
                    return False

                rowSeen[row].add(num)
                colSeen[col].add(num)
                squareSeen[square].add(num)
        
        return True