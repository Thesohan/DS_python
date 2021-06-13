"""
There are several ways of solving this problem. A basic algorithm would be to check on each node where the maximum value of its left sub-tree is less than the node’s data and the minimum value of its right sub-tree is greater than the node’s data. This is highly inefficient as for each node, both of its left and right sub-trees are explored.

Another approach would be to do a regular in-order traversal and in each recursive call, pass maximum and minimum bounds to check whether the current node’s value is within the given bounds.
"""
def is_bst_util(root,max_value,min_value):
  if root==None:
    return True
  if root.data<min_value or root.data>max_value:
    return False
  return is_bst_util(root.left,root.data,min_value) and is_bst_util(root.right,max_value,root.data)

def is_bst(root):
  #TODO: Write - Your - Code
  return is_bst_util(root,float("infinity"),float("-infinity"))

def is_bst_rec(root, min_value, max_value):
  if root == None:
    return True