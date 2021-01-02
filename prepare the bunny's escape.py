def solution(m):
    width, height = len(m[0]), len(m)

    # 1 more than 400 which is max element
    minimum = 401

    for m in every_map(m):
        minimum = min(minimum, dijkstras(m, width, height))

        if minimum == (width + height - 1):
            return minimum

    return minimum

def dijkstras(m, w, h):
    # save dict of path lengths
    d = {1: {(0, 0)}}

    # path_len starts at 2 since path_len=1 is covered by (0, 0)
    path_len = 2
    # maximum path size is 400 since max input matrix is 20x20
    while path_len < 401 and d[path_len-1]:

        #fill fringe set
        fringe = set()
        for node in d[path_len-1]:
            # expand node to include all neighbours that you haven't already visited
            for node2 in find_neighbours(node, m, w, h):
                for visited in d.values():
                    #if our node has not been visited, find its union with the fringe set
                    if node2 not in visited:
                        current = {node2}
                        fringe = fringe | current

        # check if we found exit at bottom right corner of matrix
        if (h-1, w-1) in fringe:
            return path_len

        # using current path length, set your current fringe set to the value at the path length in the visited dictionary
        d[path_len] = fringe
        # increase path length to account for moving a space away from original point
        path_len += 1

    return 401

def every_map(m):
    # base map needs to be yielded
    yield m

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]:
                copy = [[column for column in row] for row in m]

                copy[i][j] = 0

                # yield every copy of the map replacing each 1 with a 0
                yield copy

def find_neighbours(node, m, w, h):
    # find all neighbouring nodes
    x, y = node
    candidates = {(x-1, y), (x, y-1), (x+1, y), (x, y+1)}
    neighbours = set()
    for node2 in candidates:
        x2, y2 = node2
        if x2 >= 0 and x2 < h and y2 >= 0 and y2 < w and m[x2][y2] == 0:
            neighbours.add(node2)

    return neighbours

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))