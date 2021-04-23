


def partition(a,beg,end):
    """

    :param a:  [123,23,1,23,5,3,23,0,-1]
    :param beg: 0
    :param end: 8
    :return:
    """
    i=beg-1 #1
    pivot=a[end] #-1
    for j in range(beg,end): # (0,8)
        if pivot>a[j]: #-1>123
            i+=1
            a[i],a[j]=a[j],a[i]
    i+=1
    a[i],a[end]=a[end],a[i] #c
    return i

def quick_sort(a,beg,end):
    """
    :param a:     [123,23,1,23,5,3,23,0,-1]
    :param beg: 2
    :param end: 7
    :return:
    """
    if beg<end:
        pi=partition(a,beg,end)
        #first pi=
        quick_sort(a,beg,pi-1) #[123,23,1,23,5,3,23,0,-1]
        quick_sort(a,pi+1,end)


if __name__=='__main__':
    a=[123,23,1,23,5,3,23,0,-1]
    quick_sort(a,0,len(a)-1)
    print(a)