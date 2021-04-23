"""
Problem Description

Given two integer array A and B, you have to pick one element from each array such that their xor is maximum.

Return this maximum xor value.

Problem Constraints
1 <= |A|, |B| <= 105

1 <= A[i], B[i] <= 109


Input Format
First argument is an integer array A.

Second argument is an integer array B.


Output Format
Return an integer denoting the maximum xor value as described in the question.

Example Input
Input 1:

 A = [1, 2, 3]
 B = [4, 1, 2]


Example Output
Output 1:

 7

Example Explanation
Explanation 1:

 Pick A[2] and B[0] because their xor value is maximum. 3 ^ 4 = 7
"""


class Node:
    def __init__(self):
        self.children = {}  # Will be a map of T/F--> Node
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def get_child(self, item, bit_index):
        if (item & (1 << bit_index)) != 0:
            return True
        return False

    @staticmethod
    def get_node(self):
        return Node()

    def insert(self, item):

        current_root = self.root
        for i in range(31, -1, -1):  # 32 bit
            child = self.get_child(item, i)
            if not current_root.children.get(child):
                current_root.children[child] = self.get_node()
            current_root = current_root.children.get(child)
        current_root.leaf = True

    def get_xor(self, item):
        current_root = self.root
        ans = 0
        for i in range(31, -1, -1):
            child = self.get_child(item, i)
            child_to_be_found = child ^ 1
            if child_to_be_found in current_root.children:
                ans = ans + (1 << i)
                current_root = current_root.children[child_to_be_found]
            else:
                current_root = current_root.children[child]
        return ans


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        trie = Trie()
        for item in A:
            trie.insert(item)
        ans = 0
        for item in B:
            ans = max(ans, trie.get_xor(item))
        return ans


if __name__=='__main__':
    a=[1,2,3]
    b=[4,1,2]
    s=Solution()
    ans=s.solve(a,b)
    print(ans)