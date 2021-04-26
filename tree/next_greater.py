"""
Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97
Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def leftest_node(self, A):
        ans = None
        while A:
            ans = A
            A = A.left
        return ans

    def getSuccessor(self, A, B):
        if not A:
            return None
        next_greater = None
        while A:
            if A.val > B:
                next_greater = A
                A = A.left
            elif A.val < B:
                A = A.right
            elif A.val == B:
                if A.right:
                    return self.leftest_node(A.right)
                else:
                    return next_greater


