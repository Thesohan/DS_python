"""
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2
Example:
Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).
Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.
"""


def find_triplet(arr):

    hash_map={}
    for index,c in enumerate(arr):
        hash_map[c*c]=index

    for i,a in enumerate(arr):
        for j,b in enumerate(arr):
            ab_square_sum=a*a+b*b
            if hash_map.get(ab_square_sum) and hash_map[ab_square_sum] not in [i,j]:
                return True
    return False



if __name__=='__main__':
    arr=list(map(int,input().split(' ')))
    print(find_triplet(arr))
    import heapq