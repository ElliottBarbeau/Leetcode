from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []

    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = min_heap[0].interval
    while min_heap:
        queueTop = heappop(min_heap)
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end, queueTop.interval.start))
            previousInterval = queueTop.interval
        else:
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(min_heap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex, queueTop.intervalIndex + 1))


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
