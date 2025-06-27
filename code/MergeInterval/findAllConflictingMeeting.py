'''Problem 1: Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
    def findAllConflictingAppointments(self, intervals):
        intervals.sort(key=lambda x: x.start)
        conflicts = []
        previous = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current.start < previous.end:
                conflicts.append([previous, current])
            if current.end > previous.end:
                # only update previous if current ends after previous
                # this ensures we always have the latest interval that can conflict with the next one
                previous = current
        return conflicts


def main():
    sol = Solution()
    appointments = [Interval(4, 5), Interval(2, 3), Interval(
        3, 6), Interval(5, 7), Interval(7, 8)]
    conflicts = sol.findAllConflictingAppointments(appointments)
    print(len(conflicts), "conflicting appointments found:")
    for conflict in conflicts:
        conflict[0].print_interval()
        print(" and ", end='')
        conflict[1].print_interval()
        print(" conflict.")


if __name__ == "__main__":
    main()
