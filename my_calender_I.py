# import bisect
# class MyCalendar:
#
#     def __init__(self):
#         self.intervals = []
#
#
#     def book(self, start: int, end: int) -> bool:
#         if end <= start:
#             return False
#
#         i = bisect.bisect_right(self.intervals, start)
#         if i % 2:            # start is in some stored interval
#             return False
#
#         j = bisect.bisect_left(self.intervals, end)
#         if i != j:
#             return False
#
#         self.intervals[i:i] = [start, end]
#         return True

# Using Binary Tree

class Node:
    def __init__(self, s, e):
        self.e = e
        self.s = s
        self.left = None
        self.right = None


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book_helper(self, s, e, node):
        if s >= node.e:
            if node.right:
                return self.book_helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif e <= node.s:
            if node.left:
                return self.book_helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.book_helper(start, end, self.root)

my_calender = MyCalendar()
print(my_calender.book(10, 20))
print(my_calender.book(15, 25))
print(my_calender.book(20, 30))