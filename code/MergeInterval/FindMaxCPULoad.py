'''We are given a list of Jobs. Each job has a Start time, an End time, 
and a CPU load when it is running. Our goal is to find the maximum CPU load at any 
time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, 
their maximum CPU load (3+4=7) will be when both the jobs are running at the same time 
i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, 
therefore we will take the maximum load of any job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time 
interval [3,4].'''

from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load

# You can override/modify __lt__ as per your need
# setattr(Job, "__lt__", lambda self, other: write logic here)


class Solution1:
    def findMaxCPULoad(self, jobs):
        max_cpu_load = jobs[0].cpuLoad
        # TODO: Write your code here
        jobs.sort(key=lambda x: x.start)
        for i in range(1, len(jobs)):
            if jobs[i].start < jobs[i-1].end:
                max_cpu_load += jobs[i].cpuLoad
            max_cpu_load = max(max_cpu_load, jobs[i].cpuLoad)
        return max_cpu_load


# class job:
#  def __init__(self, start, end, cpu_load):
#    self.start = start
#    self.end = end
#    self.cpuLoad = cpu_load
# You can override/modify __lt__ as per your need
setattr(Job, "__lt__", lambda self, other: self.end < other.end)


class Solution2:
    def findMaxCPULoad(self, jobs):
        # sort the jobs by start time
        jobs.sort(key=lambda x: x.start)
        max_cpu_load, current_cpu_load = 0, 0
        min_heap = []

        for j in jobs:
            # remove all the jobs that have ended
            while (len(min_heap) > 0 and j.start >= min_heap[0].end):
                current_cpu_load -= min_heap[0].cpuLoad
                heappop(min_heap)
            # add the current job into min_heap
            heappush(min_heap, j)
            current_cpu_load += j.cpuLoad
            max_cpu_load = max(max_cpu_load, current_cpu_load)
        return max_cpu_load


def main():
    sol = Solution()
    print("Maximum CPU load at any time: " +
          str(sol.findMaxCPULoad([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " +
          str(sol.findMaxCPULoad([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " +
          str(sol.findMaxCPULoad([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()
