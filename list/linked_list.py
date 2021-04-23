class Node:
    def __init__(self, value, nxt):
        self.nxt = nxt
        self.value = value


class LinkedList:

    def __init__(self, node):
        self.head = node

    def insert_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_end(self,value):
        node = Node(value,None)
        temp = self.head
        while temp.nxt:
            temp=temp.nxt
        temp.nxt=node

    def insert_after_index(self,value,index):
        """
        insert a value in the given index, if index is greater than the existing size do nothing.
        """
        temp= self.head
        while index and temp.nxt:
            index-=1
            temp=temp.nxt
        if temp.nxt:
            node = Node(value,temp.nxt)
            temp.nxt=node
        else:
            print("Index is greater than the size of list")

# 0-->10   --> 99  -->12

    def print_list(self):
        temp_head = self.head
        result = ''
        while temp_head:
            result += str(temp_head.value) + '--->'
            temp_head = temp_head.nxt
        print(result)


if __name__ == '__main__':
    ll = LinkedList(Node(0, None))
    ll.insert_end(10)
    ll.insert_end(12)
    ll.insert_after_index(99,1)
    ll.insert_after_index(12,0)

    ll.print_list()
