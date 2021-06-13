def merge_sorted(head1, head2):

    #TODO: Write - Your - Code
    # head1 will always be small
    if head1==None:
        return head2
    if head2==None:
        return head1
    if head1==None and head2==None:
        return None
    if head1.data>head2.data:
        head1,head2=head2,head1
    result_head=head1
    ans=result_head
    head1=head1.next
    while head1!=None and head2!=None:
        if head1.data>head2.data:
            result_head.next=head2
            head2=head2.next
        else:
            result_head.next=head1
            head1=head1.next
        result_head=result_head.next

    if head2!=None:
        result_head.next=head2

    if head1!=None:
        result_head.next=head1

    return ans
