# minimum stack problem solution using linked list

class Node:
    def __init__(self, val, next=None, min=None):
        self.val = val
        self.next = next
        self.min = min

class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val, None, val)
        else:
            self.head = Node(val, self.head, min(val, self.head.min))

    def pop(self):
        if self.head is None:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.val

    def getMin(self):
        if self.head is None:
            return None
        else:
            return self.head.min