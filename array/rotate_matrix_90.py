"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified

    def reverse(self, A):
        for col_index in range(self.col_len):
            for row_index in range(self.row_len // 2):
                A[row_index][col_index], A[self.row_len - 1 - row_index][col_index] = A[self.row_len - 1 - row_index][
                                                                                          col_index], A[row_index][
                                                                                          col_index]

        # print(A)

    def transpose(self, A):
        for row in range(self.row_len):
            for col in range(self.col_len):
                if row < col:
                    A[row][col], A[col][row] = A[col][row], A[row][col]

    def rotate(self, A):
        self.row_len = len(A)
        self.col_len = len(A[0])
        self.reverse(A)
        self.transpose(A)
        return A
