# Given a 2D board and a word, find if the word exists in the grid.
#The word must be constructed from letters of sequentially adjacent cells (horizontally or vertically). Each cell may only be used once.

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        # Mark the cell as visited
        temp, board[r][c] = board[r][c], '#'
        # Explore neighbors
        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))
        # Restore the cell
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True

    return False

# Example
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(exist(board, "ABCCED"))  # Output: True