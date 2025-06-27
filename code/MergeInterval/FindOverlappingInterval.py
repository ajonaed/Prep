'''Problem 1: Given a set of intervals, find out if any two intervals overlap.

Example:

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def print_interval(i):
    print("[" + str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def find_overlapping_interval(self, intervals):
        if len(intervals) < 2:
            return False

        # sort the intervals on the start time
        intervals.sort(key=lambda x: x.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start <= end:  # overlapping intervals
                return True

        return False


def main():

    sol = Solution()
    print("Overlapping intervals: ", end='')
    print(sol.find_overlapping_interval(
        [Interval(1, 4), Interval(2, 5), Interval(7, 9)]))  # True
    print(sol.find_overlapping_interval(
        [Interval(6, 7), Interval(2, 4)]))  # False
    print(sol.find_overlapping_interval(
        [Interval(1, 4), Interval(2, 6), Interval(3, 5)]))  # True


main()
