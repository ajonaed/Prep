'''Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(i):
        print("[" + str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def merge(self, intervals_a, intervals_b):
        result = []
        i, j = 0, 0

        while i < len(intervals_a) and j < len(intervals_b):
            a_after_b = intervals_a[i].start >= intervals_b[j].start and intervals_a[i].start <= intervals_b[j].end
            b_after_a = intervals_b[j].start >= intervals_a[i].start and intervals_b[j].start <= intervals_a[i].end
            if a_after_b or b_after_a:
                start = max(intervals_a[i].start, intervals_b[j].start)
                end = min(intervals_a[i].end, intervals_b[j].end)
                result.append(Interval(start, end))
            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1

        return result


def main():
    sol = Solution()
    intervals_a = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    intervals_b = [Interval(2, 3), Interval(5, 7)]
    print("Intervals Intersection: ", end="")
    k = sol.merge(intervals_a, intervals_b)
    for interval in k:
        Interval.print_interval(interval)
    print("\n")
    intervals_a = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
    intervals_b = [Interval(5, 10)]
    print("Intervals Intersection: ", end="")
    k = sol.merge(intervals_a, intervals_b)
    for interval in k:
        Interval.print_interval(interval)


main()
