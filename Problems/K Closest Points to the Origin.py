import math
from heapq import *
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.euclidean_distance = -(x**2 + y**2)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def __lt__(self, other):
        return self.euclidean_distance < other.euclidean_distance


def find_closest_points(points, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k, len(points)):
        if points[i].euclidean_distance < -maxHeap[0].euclidean_distance:
            heappushpop(maxHeap, points[i])
    return list(maxHeap)


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
