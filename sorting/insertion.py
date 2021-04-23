def insertion_sort(A:list)-> list:
    """
    Ex. A=[2,3,1,5,6,0]
    :param A:
    :return:
    """
    for i in range(1,len(A)):
        item=A[i]
        index=i-1
        while index>=0 and item<A[index]:
            A[index+1]=A[index]
            index-=1
        A[index+1]=item
    return A


if __name__=='__main__':
    a=[23,12,3,1,4,5]
    a=insertion_sort(a)
    print(a)



