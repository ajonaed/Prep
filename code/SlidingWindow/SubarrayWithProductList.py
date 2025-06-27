'''Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Note: This problem is very similar to the previous one. Here, we are trying to find all the subarrays, whereas in the previous problem, we focused on finding only the count of such subarrays.

Example 1:

Input: [2, 5, 3, 10], target=30                                              
Output: [2], [5], [2, 5], [3], [5, 3], [10]                           
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50                                              
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]                         
Explanation: There are seven contiguous subarrays whose product is less than the target.
Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 1000
0 <= k <= 106
'''

class Solution:
  #Time Complexity: O(N^2) where N is the length of the input array.
  #Space Complexity: O(N^3) for storing the resultant subarrays.
  def findSubarrays(self, arr, target):
      # Resultant list to store all valid subarrays.
      result = []

      # Variable to store the product of elements in the current subarray.
      product = 1.0

      # Left boundary of the current subarray.
      left = 0

      # Iterate over the array using 'right' as the right boundary of the current subarray.
      for right in range(len(arr)):
          # Update the product with the current element.
          product *= arr[right]

          # If the product is greater than or equal to the target, slide the left boundary to 
          # the right until product is less than target.
          while product >= target and left < len(arr):
              product /= arr[left]
              left += 1

          # Create a temporary list to store the current subarray.
          temp_list = []

          # Iterate from 'right' to 'left' and add all these subarrays to the result.
          for i in range(right, left - 1, -1):
              # Add the current element at the beginning of the list.
              temp_list.insert(0, arr[i])

              # Add the current subarray to the result.
              result.append(list(temp_list))

      # Return the result.
      return result


# Example usage
sol = Solution()
print(sol.findSubarrays([2, 5, 3, 10], 30))
print(sol.findSubarrays([8, 2, 6, 5], 50))
