def deleteDuplication(root):
    pre_node = None
    cur_node = root
    while cur_node:
        if cur_node.next and \
                cur_node.next.value == cur_node.value:
            value = cur_node.value
            deleted = cur_node
            while deleted and deleted.value == value:
                deleted = deleted.next
            cur_node = deleted
            pre_node.next = cur_node
        else:
            pre_node = cur_node
            cur_node = cur_node.next
