"""
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].

"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversalHelper(self, A):
        if A:
            ans.append(A.val)
            self.preorderTraversalHelper(A.left)

            self.preorderTraversalHelper(A.right)

    def preorderTraversal(self, A):
        global ans
        ans = []
        self.preorderTraversalHelper(A)
        return ans


# Without using Recursion:

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversalHelper(self, A):
        stack = [A]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def preorderTraversal(self, A):
        global ans
        ans = []
        self.preorderTraversalHelper(A)
        return ans
