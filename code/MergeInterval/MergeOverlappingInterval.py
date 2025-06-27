'''Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].
Image
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def print_interval(i):
    print("[" + str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    # Time complexity: O(N log N) where N is the number of intervals
    # Space complexity: O(N) for the output list
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        # sort the intervals on the start time
        intervals.sort(key=lambda x: x.start)

        mergedIntervals = []
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:  # overlapping intervals, adjust the 'end'
                end = max(interval.end, end)
            else:  # non-overlapping interval, add the previous interval and reset
                mergedIntervals.append(Interval(start, end))
                start = interval.start
                end = interval.end

        # add the last interval
        mergedIntervals.append(Interval(start, end))
        return mergedIntervals


def main():
    sol = Solution()
    print("Merged intervals: ", end='')
    for i in sol.merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        print_interval(i)
    print()

    print("Merged intervals: ", end='')
    for i in sol.merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        print_interval(i)
    print()

    print("Merged intervals: ", end='')
    for i in sol.merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        print_interval(i)
    print()


main()


"""Abdullah Jonaed is a dedicated and community-driven real estate professional based in New York. With a strong background in customer service and a passion for helping others, Abdullah brings a people-first approach to real estate.

Fluent in Bengali and known for his tech-savviness and negotiation skills, Abdullah specializes in residential homes, first-time buyers, condos, and investment properties. Whether you're purchasing your first home or expanding your investment portfolio, Abdullah is committed to guiding you every step of the way with integrity and a focus on your goals.

Proud to have recently joined EXIT Realty, Abdullah is ready to put his skills and local knowledge to work for you."""


A dedicated and community-driven real estate professional based in New York. With a strong background in customer service and a passion for helping others, I bring a people-first approach to the real estate industry.
Fluent in Bengali and known for his tech-savviness and negotiation skills, Abdullah specializes in residential homes, first-time buyers, condos, and investment properties. Whether you're purchasing your first home or expanding your investment portfolio, I am committed to guiding you every step of the way with integrity and a focus on your goals.
Proud to have recently joined EXIT Realty.