def build_range_tree(points):
    if not points:
        return None

    points.sort(key=lambda p: p[0])

    median_index = len(points) // 2
    median_point = points[median_index]

    node = {
        'point': median_point,
        'left': build_range_tree(points[:median_index]),
        'right': build_range_tree(points[median_index + 1:])
    }

    return node


def range_query(node, x1, x2, y1, y2, result):
    if node is None:
        return

    if x1 <= node['point'][0] <= x2 and y1 <= node['point'][1] <= y2:
        result.append(node['point'])

    if node['point'][0] >= x1:
        range_query(node['left'], x1, x2, y1, y2, result)
    if node['point'][0] <= x2:
        range_query(node['right'], x1, x2, y1, y2, result)


points = [(2, 5), (1, 3), (4, 7), (6, 2), (8, 9), (5, 4)]
tree = build_range_tree(points)
result = []
range_query(tree, 2, 6, 3, 7, result)

for point in result:
    print(point)