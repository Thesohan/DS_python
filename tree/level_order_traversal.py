def level_order_traversal(root):
    result = ""
    # TODO: Write - Your - Code
    from collections import deque
    dq=deque()
    dq.append(root)
    while dq:
        temp_nodes=[]
        while dq:
            root=dq.popleft()
            temp_nodes.append(root)
            result+=str(root.data)+" "
        # result+=";"
        for node in temp_nodes:
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return result