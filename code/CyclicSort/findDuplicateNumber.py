'''We are given an unsorted array containing n+1 numbers taken from the range 1 to n. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however, 
allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
'''


class Solution:
    def find_duplicate(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:  # Check if the current element is in its correct position
                # Calculate the correct index for the current element
                j = nums[i] - 1
                # Check if the current element is not equal to the element at its correct index
                if nums[i] != nums[j]:
                    # Swap the elements to their correct positions
                    nums[i], nums[j] = nums[j], nums[i]
                else:  # We have found the duplicate
                    return nums[i]
            else:
                i += 1  # Move to the next element

        return -1  # No duplicate found


def main():
    sol = Solution()
    print(sol.find_duplicate([1, 4, 4, 3, 2]))
    print(sol.find_duplicate([2, 1, 3, 3, 5, 4]))
    print(sol.find_duplicate([2, 4, 1, 4, 4]))


main()
'''
Own Solution
class Solution:
  def findNumber(self, nums):
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < len(nums):
      j = nums[i] - 1
      if nums[i] <= n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i += 1
    print(nums)
    for i in range(n):
      if nums[i] != i + 1:
        return nums[i]
    return -1
'''
