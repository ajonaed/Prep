'''Given an unsorted array containing numbers and a number ‘k’, 
find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
1 <= k <= 1000
'''

class SolutionOwn:
  def findNumbers(self, nums, k):
    missingNumbers = []
    # TODO: Write your code here
    i, n = 0, len(nums)

    while i < n:
      j = nums[i] - 1
      if 1<= nums[i] <= n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # Swap
      else:
        i += 1
    
    extraSeen = set()
    for i in range(n):
      if len(missingNumbers) < k and nums[i] != i + 1:
        missingNumbers.append(i+1)
        extraSeen.add(nums[i])
    i = 1
    while len(missingNumbers) < k:
      nextNumber = i + n
      if nextNumber not in extraSeen:
        missingNumbers.append(nextNumber)
      i += 1
    return missingNumbers

class Solution:
  '''The time complexity of the above and below algorithm is , 
  as the last two for loops will run for O(n) and O(k) times respectively.
  The algorithm needs O(k) space to store the extraNumbers.'''
  def findNumbers(self, nums, k):
    n = len(nums)
    i = 0
    while i < len(nums):
      j = nums[i] - 1
      if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # Swap the current element with its correct position.
      else:
        i += 1

    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
      if len(missingNumbers) < k:
        if nums[i] != i + 1:
          missingNumbers.append(i + 1)  # Add the missing number to the result list.
          extraNumbers.add(nums[i])     # Keep track of extra numbers encountered.

    # Add the remaining missing numbers
    i = 1
    while len(missingNumbers) < k:
      candidateNumber = i + n
      # Ignore if the array contains the candidate number
      if candidateNumber not in extraNumbers:
        missingNumbers.append(candidateNumber)  # Add remaining missing numbers to the result list.
      i += 1

    return missingNumbers


def main():
  sol = Solution()
  print(sol.findNumbers([3, -1, 4, 5, 5], 3))
  print(sol.findNumbers([2, 3, 4], 3))
  print(sol.findNumbers([-2, -3, 4], 2))


main()
