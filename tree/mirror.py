"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

https://leetcode.com/problems/symmetric-tree/

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        return (left.val == right.val) and self.isMirror(left.right, right.left) and self.isMirror(left.left,
                                                                                                   right.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

"""
Another solution (Iterative)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    sorted
    def isSymmetric(self, root: TreeNode) -> bool:
        stack=[root,root]
        while stack:
            root1=stack.pop()
            root2=stack.pop()
            if root1==None and root2==None:
                continue
            if  (root1==None or root2==None)or (root1.val!=root2.val):
                return False
            stack.extend([root1.left,root2.right])
            stack.extend([root1.right,root2.left])
        return True
