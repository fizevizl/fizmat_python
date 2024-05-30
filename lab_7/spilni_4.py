import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def point_to_side_distance(x, y, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dot_product = (x - x1) * dx + (y - y1) * dy
    length_squared = dx ** 2 + dy ** 2
    projection = dot_product / length_squared
    if projection <= 0:
        return distance(x, y, x1, y1)
    if projection >= 1:
        return distance(x, y, x2, y2)
    proj_x = x1 + projection * dx
    proj_y = y1 + projection * dy
    return distance(x, y, proj_x, proj_y)

def point_to_triangle_distance(x, y, x1, y1, x2, y2, x3, y3):
    dist1 = point_to_side_distance(x, y, x1, y1, x2, y2)
    dist2 = point_to_side_distance(x, y, x2, y2, x3, y3)
    dist3 = point_to_side_distance(x, y, x3, y3, x1, y1)
    return min(dist1, dist2, dist3)

x1, y1 = 1, 1
x2, y2 = 5, 1
x3, y3 = 3, 4
x, y = 2, 2

result = point_to_triangle_distance(x, y, x1, y1, x2, y2, x3, y3)
print(result)

