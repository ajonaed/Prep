'''Given an array, 
find the average of each subarray of K contiguous elements in it.'''

class Solution:
    '''Brute force solution
    Time complexity: O(N*K)'''
    def findAverages(self, K, arr):
        res = []
        for i in range(len(arr)-K+1):
            sum = 0.0
            for j in range(i, i+K):
                sum += arr[j]
            res.append(sum/K)
        return res


class Solution2:
    '''Optimized solution using sliding window
    Time complexity: O(N)
    Space complexity: O(1)'''
    def findAverages(self, K, arr):
        res = []
        windowSum, windowStart = 0.0, 0
        for i in range(len(arr)):
            windowSum += arr[i]
            if i >= K - 1:
                res.append(windowSum / K)  # calculate the average
                windowSum -= arr[windowStart]  # subtract the element going out
                windowStart += 1  # slide the window ahead
        return res


def main():
  sol = Solution()
  result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

  sol1 = Solution2()
  result = sol1.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K by Sol1: " + str(result))


main()