def intersection_of_two_linked_list(headA, headB):
    a, b = headA, headB
    while (a != b):
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a