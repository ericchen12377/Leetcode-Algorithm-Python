def merge_k_lists(lists: list) -> ListNode:
    # base-condition checks
    if not lists:
        return
    elif len(lists) == 1:
        return lists[0]
    
    result = []
    
    for node in lists:
        while node:
            result.append(node.val)
            node = node.next
    
    result.sort()
    
    # build linked-list to return
    dummy = node = ListNode()
    
    for val in result:
        node.next = ListNode(val)
        node = node.next
    
    return dummy.next