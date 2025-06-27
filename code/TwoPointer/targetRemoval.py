'''
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].'''


class Solution:
    def remove(self, arr, key):
        j = 0
        for i in range(1, len(arr)):
            if arr[i] != key:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
        # print(sorted(arr[:j]))
        # newList = arr[:j]
        # print(newList)
        # newList.sort() Inplace sort, 
        # print(newList)
        return j


k = Solution()
print(k.remove([3, 2, 3, 6, 3, 10, 9, 3], 3))

'''
class Solution:
  def remove(self, arr, key):
    # Initialize a variable to keep track of the next non-'key' element index.
    nextElement = 0

    # Iterate through the input array 'arr'.
    for i in range(len(arr)):
      if arr[i] != key:  # Check if the current element is not equal to 'key'.
        # If not equal, copy the current element to the next available position.
        arr[nextElement] = arr[i]
        # Increment the nextElement index to prepare for the next non-'key' element.
        nextElement += 1

    # Return the length of the modified array, which represents the new length.
    return nextElement


def main():
  sol = Solution()

  # Test case 1
  print("Array new length: " + str(sol.remove([3, 2, 3, 6, 3, 10, 9, 3], 3)))

  # Test case 2
  print("Array new length: " + str(sol.remove([2, 11, 2, 2, 1], 2)))


main()
'''
