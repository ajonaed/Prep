'''Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

Example 1:

Input: arr = [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: arr = [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


class Solution:
    def findMaxSumSubArray(self, k, arr):
        # TODO: Write your code here
        maxSeen = float('-inf')
        for i in range(len(arr) - k + 1):
            windowSum = 0
            for j in range(i, i+k):
                windowSum += arr[j]
                if windowSum >= maxSeen:
                    maxSeen = windowSum

        return maxSeen


class Solution1:
    def findMaxSumSubArray(self, k, arr):
        # TODO: Write your code here
        maxSeen = float('-inf')
        windowSum = 0
        startIndex = 0
        for i in range(len(arr)):
            windowSum += arr[i]
            if i >= k - 1:
                if windowSum >= maxSeen:
                    maxSeen = windowSum
                windowSum -= arr[startIndex]
                startIndex += 2
        return maxSeen


def main():
    sol = Solution()
    result = sol.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2])
    print("Averages of subarrays of size K: " + str(result))
    result = sol.findMaxSumSubArray(2, [2, 3, 4, 1, 5])
    print("Averages of subarrays of size K: " + str(result))


main()
