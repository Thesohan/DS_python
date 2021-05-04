"""
https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/
Given a matrix of ‘O’ and ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’
Difficulty Level : Medium
Last Updated : 31 Mar, 2021
Given a matrix where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it.
Examples:


Input: mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Output: mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'X', 'X', 'X'},
                      {'O', 'X', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'O', 'X', 'O'},
                      {'O', 'O', 'X', 'O', 'O', 'O'},
                    };


Input: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };


Input: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };


Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
This is mainly an application of Flood-Fill algorithm. The main difference here is that a ‘O’ is not replaced by ‘X’ if it lies in region that ends on a boundary. Following are simple steps to do this special flood fill.
1) Traverse the given matrix and replace all ‘O’ with a special character ‘-‘.
2) Traverse four edges of given matrix and call floodFill(‘-‘, ‘O’) for every ‘-‘ on edges. The remaining ‘-‘ are the characters that indicate ‘O’s (in the original matrix) to be replaced by ‘X’.
3) Traverse the matrix and replace all ‘-‘s with ‘X’s.
Let us see steps of above algorithm with an example. Let following be the input matrix.



       mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Step 1: Replace all ‘O’ with ‘-‘.

       mat[M][N] =  {{'X', '-', 'X', 'X', 'X', 'X'},
                     {'X', '-', 'X', 'X', '-', 'X'},
                     {'X', 'X', 'X', '-', '-', 'X'},
                     {'-', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', '-', 'X', '-'},
                     {'-', '-', 'X', '-', '-', '-'},
                    };
Step 2: Call floodFill(‘-‘, ‘O’) for all edge elements with value equals to ‘-‘

       mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', '-', 'X'},
                     {'X', 'X', 'X', '-', '-', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Step 3: Replace all ‘-‘ with ‘X’.

       mat[M][N] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'X', 'X', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
The following is implementation of above algorithm.
"""

class Solution:
    def is_safe(self, board, x, y):
        n = len(board)
        m = len(board[0])
        if x < n and x > -1 and y < m and y > -1:
            return True
        return False

    def flood_fill(self, board, x, y) -> None:
        if not self.is_safe(board, x, y):
            return
        if board[x][y] == '-':
            board[x][y] = 'O'
        else:
            return

        self.flood_fill(board, x + 1, y)
        self.flood_fill(board, x, y + 1)
        self.flood_fill(board, x - 1, y)
        self.flood_fill(board, x, y - 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = '-'
        print(board)
        for col in range(len(board[0])):
            if board[0][col] == '-':
                self.flood_fill(board, 0, col)
        print(board)
        for col in range(len(board[0])):
            if board[-1][col] == '-':
                self.flood_fill(board, len(board) - 1, col)
        print(board)
        for row in range(len(board)):
            if board[row][0] == '-':
                self.flood_fill(board, row, 0)
        print(board)
        for row in range(len(board)):
            if board[row][-1] == '-':
                self.flood_fill(board, row, len(board[0]) - 1)
        print(board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '-':
                    board[row][col] = 'X'



