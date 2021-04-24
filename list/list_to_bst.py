"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/
Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build_BST(self, beg, end):
        if beg <= end:
            mid = (beg + end) // 2
            left = self.build_BST(beg, mid - 1)
            root = TreeNode(val=self.head.val, left=left)
            self.head = self.head.next
            right = self.build_BST(mid + 1, end)
            root.right = right
            return root
        return None

    def find_size(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        size = self.find_size(head)
        return self.build_BST(0, size - 1)
