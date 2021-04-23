def merge_sort(A:list,beg:int,end:int)->None:
    """
    A=[12,3,1,2,3,342,2324,5]
    beg=0,end=8
    mid=(0+8)//2=4
    B=[12,3,1,2,3,342,2324,5,4]
    beg=0,end=9
    mid=(0+9)//2=4

    :param A:
    :param beg:
    :param end:
    :return:
    """
    if beg>=end:
        return
    mid = (beg+end)//2
    merge_sort(A,beg,mid)
    merge_sort(A,mid+1,end)
    merge(A,beg,mid,end)
def merge(a:list,beg:int,mid:int,end:int):
    left=a[beg:mid+1]
    right=a[mid+1:end+1]
    i=0
    j=0
    k=beg
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else :
            a[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        # print(k,i,a,left,beg)
        a[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        # print(k,j,a,right)
        a[k]=right[j]
        j+=1
        k+=1

if __name__=="__main__":
    a=[-12,3,1,2,13,342,2324,5]
    merge_sort(a,0,len(a)-1)
    print(a)
