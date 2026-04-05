from collections import defaultdict


class Solution:
    def has_duplicates(self, board_vector: list[str]) -> bool:
        """Create a non empty list for each board vector to check for the presence
        of duplicates and returns the result."""

        non_empty_vector = [num for num in board_vector if num != "."]
        return len(set(non_empty_vector)) != len(non_empty_vector)

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Checks if a 2D Sudoku Board (Filled / Partially Filled) is valid or invalid."""
        
        for vec_idx in range(len(board)):
            # Checking Row-Wise
            if self.has_duplicates(board_vector=board[vec_idx]):
                return False            

            # Checking Column-Wise
            board_vector = [board[i][vec_idx] for i in range(len(board))]
            if self.has_duplicates(board_vector=board_vector):
                return False

        # Checking Square-Wise: Iterating through the board as 3x3 Squares
        for square_n in range(9):
            # A Lookup Table for Seen Elements in each Square
            square_digest = defaultdict(int)
            for row_idx in range(3):
                for col_idx in range(3):
                    square_row = (square_n // 3) * 3 + row_idx
                    square_col = (square_n % 3) * 3 + col_idx

                    element = board[square_row][square_col]
                    if element == ".":
                        continue
                    if element in square_digest:
                        return False
                    square_digest[element] += 1
                    
        return True
