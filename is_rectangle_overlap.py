def is_rectangle_overlap(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2


print(is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]))


def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Compute the area of intersection
    x_overlap = max(0, min(ax2, bx2) - max(ax1, bx1))
    y_overlap = max(0, min(ay2, by2) - max(ay1, by1))
    overlap_area = x_overlap * y_overlap

    # Compute the area of union
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union_area = area_a + area_b - overlap_area

    return union_area


print(compute_area(0, 0, 2, 2, 1, 1, 3, 3))

