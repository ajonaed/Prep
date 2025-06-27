'''Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [13, 14], [8,12], [45, 47]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
'''

class Interval:
 def __init__(self, start, end):
   self.start = start
   self.end = end

 def print_interval(self):
   print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
    def canAttendAllAppointmentsBR(self, intervals):
        # TODO: Write your code here
        intervals.sort(key=lambda x: x.start)
        i, j = 0, 0
        while i < len(intervals)-1:
            start = intervals[i].start
            end = intervals[i].end
            j = i+1
            while j < len(intervals):
                if intervals[j].start < end:
                    return False
                j += 1
            i += 1
        return True

    def canAttendAllAppointmentsOptimal(self, intervals):
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                # please note the comparison above, it is "<" and not "<="
                # while merging we needed "<=" comparison, as we will be merging the two
                # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
                # such intervals don't represent conflicting appointments as one starts right
                # after the other
                return False
        return True


def main():
    sol = Solution()
    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointmentsBR([Interval(1, 4), Interval(2, 5), Interval(7, 9)])))
    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointmentsBR([Interval(6, 7), Interval(2, 4), Interval(8, 12)])))
    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointmentsBR([Interval(4, 5), Interval(2, 3), Interval(3, 6)])))


main()
