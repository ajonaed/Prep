'''
Given a list of intervals representing the start and end time of ‘N’ meetings, 
find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to hold all the meetings.
Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].


Similar Problems
Problem 1: Given a list of intervals, find the point where the maximum number of 
intervals overlap.

Problem 2: Given a list of intervals representing the arrival and departure times 
of trains to a train station, our goal is to find the minimum number of platforms
required for the train station so that no train has to wait.

Both of these problems can be solved using the approach discussed above.'''

import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# You can override/modify __lt__ as per your need
setattr(Meeting, "__lt__", lambda self, other: self.end < other.end)


class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if not meetings:
            return 0

        # sort the meetings by start time
        meetings.sort(key=lambda x: x.start)

        minRooms = 0
        minHeap = []
        for meeting in meetings:
            # remove all meetings that have ended
            while minHeap and meeting.start >= minHeap[0].end:
                heapq.heappop(minHeap)
            # add the current meeting into the minHeap
            heapq.heappush(minHeap, meeting)
            # all active meetings are in the minHeap, so we need rooms for all of them.
            minRooms = max(minRooms, len(minHeap))
        return minRooms


if __name__ == "__main__":
    sol = Solution()
    inputs = [
        [Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)],
        [Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)],
        [Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)],
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
    ]

    for input in inputs:
        result = sol.findMinimumMeetingRooms(input)
        print("Minimum meeting rooms required:", result)

import heapq

# You can override/modify __lt__ as per your need
setattr(Meeting, "__lt__", lambda self, other: write logic here)


class Solution2:
  def findMinimumMeetingRooms(self, meetings):
    minRooms = 0
    # TODO: Write your code here
    #track the end time
    tracker = {meetings[0].end : 1}
    #Sort
    meetings.sort(key=lambda x: x.start)
    for i in range(1, len(meetings)):
      if meetings[i].start < meetings[i-1].end:
        if meetings[i].start not in tracker.keys():
          minRooms += 1
          tracker[meetings[i].end] = minRooms
    # minRooms += 1
    # return minRooms
    return len(tracker)
