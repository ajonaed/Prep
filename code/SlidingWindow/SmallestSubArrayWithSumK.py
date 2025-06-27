'''Given an array of positive integers and a number 'S',
 find the length of the smallest contiguous subarray whose sum is greater 
 than or equal to 'S'. Return 0 if no such subarray exists.

Example 1:

Input: arr = [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: arr = [2, 1, 5, 2, 8], S=7
Output: 1 
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: arr = [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
Constraints:

1 <= S <= 
1 <= arr.length <= 105
1 <= arr[i] <= 104
'''
import math

class Solution:
  def findMinSubArray(self, s, arr):
    # TODO: Write your code here
    winSum, startIndex = 0, 0
    minLength = float('inf')
    for endIndex in range(len(arr)):
      winSum += arr[endIndex]
      while winSum >= s:
        minLength = min(minLength, endIndex - startIndex + 1)
        winSum -= arr[startIndex]
        startIndex += 1

    return minLength if minLength != math.inf else 0

'''Brute force approach: O(n^2) time complexity and O(1) space complexity.
   We can use two nested loops to find the sum of all subarrays and check if it is greater than or equal to 'S'. 
   If it is, we can update the minimum length of the subarray. 
   This approach is not efficient for large arrays, but it works for small arrays.
'''
def smallest_subarray_with_given_sum_brute_force(s, arr):
    min_length = math.inf

    for start in range(len(arr)):
        current_sum = 0
        for end in range(start, len(arr)):
            current_sum += arr[end]
            if current_sum >= s:
                min_length = min(min_length, end - start + 1)
                break  # No need to keep going, it will only get longer

    return min_length if min_length != math.inf else 0
def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(8, [3, 4, 1, 1, 6])))

main()